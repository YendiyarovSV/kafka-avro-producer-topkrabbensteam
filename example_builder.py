from kafkaSchemaManager.decorator.commandCenterEnum import CommandCenterEnum
from kafkaSchemaManager.implementation.config.JsonKafkaConfig import JsonKafkaConfig
from kafkaSchemaManager.builders.commandCenterInstanceManager import CommandCenterInstanceManager
from kafkaSchemaManager.builders.commandCenterBuilder import CommandCenterBuilder
from kafkaSchemaManager.implementation.config.SimpleKafkaConfig import SimpleKafkaConfig

#task is to produce multiple messages to different Kafka topics (e.g. we want to produce to Topics: Topic1 and Topic2)

#create KafkaConfig
kafkaConfig = SimpleKafkaConfig("http://172.17.217.108:8083","172.17.217.108:6667")

#create commandCenterBuilder
commandCenterBuilder = CommandCenterBuilder().getBuilder()\
    .setCommandCenterId(CommandCenterEnum.LocalKafkaStorageCommandCenter)\
    .setKafkaConfig(kafkaConfig)

#create commandCenterInstance manager
commandCenterInstanceManager = CommandCenterInstanceManager(commandCenterBuilder)

#create or fetch commandCenter if exist
topic1DataCommandCenter = commandCenterInstanceManager.fetchOrCreateCommandCenterByTopicName("raw_data")
topic2DataCommandCenter = commandCenterInstanceManager.fetchOrCreateCommandCenterByTopicName("Topic2")






