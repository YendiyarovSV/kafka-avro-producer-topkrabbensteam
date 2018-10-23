from kafkaSchemaManager.decorator.CommandCenterFactory import CommandCenterFactory
from kafkaSchemaManager.decorator.commandCenterEnum import CommandCenterEnum
from kafkaSchemaManager.implementation.postgreBootstrap.parserKafkaSchemaHolder import ParserKafkaSchemaHolder
from kafkaSchemaManager.implementation.postgreBootstrap.postgreSqlOperations import PostgreSqlOperations
from kafkaSchemaManager.implementation.config.postgreSqlLocalConfig import PostgreSqlLocalConfig
from kafkaSchemaManager.implementation.config.JsonKafkaConfig import JsonKafkaConfig

from kafkaSchemaManager.implementation.schemaMigration.schemaCreation import CreateSchema
from kafkaSchemaManager.implementation.localSchema.JsonLocalSchemaLoader import JsonLocalSchemaLoader

'''
commandCenter = CommandCenterFactory.createCommandCenter(CommandCenterEnum.LocalStorageCommandCenter,
                                                         "testTopic",
                                                         JsonKafkaConfig("config.json"),
                                                         None, 
                                                         "localMigrationTopic.json")
'''

'''
commandCenter = CommandCenterFactory.createCommandCenter(CommandCenterEnum.LocalKafkaStorageCommandCenter,
                                                         "raw_data",
                                                         JsonKafkaConfig("config.json"),
                                                         None, 
                                                         None)
'''





commandCenter = CommandCenterFactory.createCommandCenter(CommandCenterEnum.PostgreeSqlCommandCenter,
                                                         "raw_data",
                                                         JsonKafkaConfig("config.json"),
                                                         PostgreSqlLocalConfig(),
                                                         None)


##KafkaConfig
print(commandCenter.GetKafkaSchemaOperations().checkIfSchemaExists(commandCenter.GetLocalSchemaHolder().getSchemaName()))
print(commandCenter.GetKafkaSchemaOperations().getKafkaSchemaVersion(commandCenter.GetLocalSchemaHolder().getSchemaName()))
print(commandCenter.IsKafkaSchemaIsOutdated())

#commandCenter.UpdateKafkaSchema()
#commandCenter.AddNullStringSchemaField("jedi00087","my new command field")

commandCenter.UpdateLocalSchemaAndThenUpdateServerKafkaSchema()
commandCenter.ProduceKafkaMessage({"Email":"seregae@e1.ru","ParserName": "must have", "myNewBrandField2": "Hello world"})


#update localSchema from newly create one
createdLocalSchemaHolder = CreateSchema("testTopic","localMigrationTopic.json")
commandCenter.localSchemaHolder = createdLocalSchemaHolder
commandCenter.UpdateLocalSchema()


#update localSchema from
localSchemaJson = JsonLocalSchemaLoader("localMigrationTopic.json","testTopic").loadLocalSchema()