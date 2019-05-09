# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.datalabeling_v1beta1.proto import (
    annotation_spec_set_pb2 as google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_annotation__spec__set__pb2,
)
from google.cloud.datalabeling_v1beta1.proto import (
    data_labeling_service_pb2 as google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2,
)
from google.cloud.datalabeling_v1beta1.proto import (
    dataset_pb2 as google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2,
)
from google.cloud.datalabeling_v1beta1.proto import (
    instruction_pb2 as google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_instruction__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DataLabelingServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateDataset = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateDataset",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.CreateDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.GetDataset = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetDataset",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.ListDatasets = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListDatasets",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDatasetsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDatasetsResponse.FromString,
        )
        self.DeleteDataset = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteDataset",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteDatasetRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ImportData = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ImportData",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ImportDataRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ExportData = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ExportData",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ExportDataRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetDataItem = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetDataItem",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetDataItemRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.DataItem.FromString,
        )
        self.ListDataItems = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListDataItems",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDataItemsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDataItemsResponse.FromString,
        )
        self.GetAnnotatedDataset = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetAnnotatedDataset",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetAnnotatedDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.AnnotatedDataset.FromString,
        )
        self.ListAnnotatedDatasets = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListAnnotatedDatasets",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotatedDatasetsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotatedDatasetsResponse.FromString,
        )
        self.DeleteAnnotatedDataset = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteAnnotatedDataset",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteAnnotatedDatasetRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.LabelImage = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelImage",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelImageRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.LabelVideo = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelVideo",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelVideoRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.LabelText = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelText",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelTextRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.LabelAudio = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelAudio",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelAudioRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetExample = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetExample",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetExampleRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.Example.FromString,
        )
        self.ListExamples = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListExamples",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListExamplesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListExamplesResponse.FromString,
        )
        self.CreateAnnotationSpecSet = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateAnnotationSpecSet",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.CreateAnnotationSpecSetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_annotation__spec__set__pb2.AnnotationSpecSet.FromString,
        )
        self.GetAnnotationSpecSet = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetAnnotationSpecSet",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetAnnotationSpecSetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_annotation__spec__set__pb2.AnnotationSpecSet.FromString,
        )
        self.ListAnnotationSpecSets = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListAnnotationSpecSets",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotationSpecSetsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotationSpecSetsResponse.FromString,
        )
        self.DeleteAnnotationSpecSet = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteAnnotationSpecSet",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteAnnotationSpecSetRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateInstruction = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateInstruction",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.CreateInstructionRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetInstruction = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetInstruction",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetInstructionRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_instruction__pb2.Instruction.FromString,
        )
        self.ListInstructions = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListInstructions",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListInstructionsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListInstructionsResponse.FromString,
        )
        self.DeleteInstruction = channel.unary_unary(
            "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteInstruction",
            request_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteInstructionRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class DataLabelingServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def CreateDataset(self, request, context):
        """Creates dataset. If success return a Dataset resource.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetDataset(self, request, context):
        """Gets dataset by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListDatasets(self, request, context):
        """Lists datasets under a project. Pagination is supported.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteDataset(self, request, context):
        """Deletes a dataset by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ImportData(self, request, context):
        """Imports data into dataset based on source locations defined in request.
    It can be called multiple times for the same dataset. Each dataset can
    only have one long running operation running on it. For example, no
    labeling task (also long running operation) can be started while
    importing is still ongoing. Vice versa.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportData(self, request, context):
        """Exports data and annotations from dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetDataItem(self, request, context):
        """Gets a data item in a dataset by resource name. This API can be
    called after data are imported into dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListDataItems(self, request, context):
        """Lists data items in a dataset. This API can be called after data
    are imported into dataset. Pagination is supported.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAnnotatedDataset(self, request, context):
        """Gets an annotated dataset by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListAnnotatedDatasets(self, request, context):
        """Lists annotated datasets for a dataset. Pagination is supported.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteAnnotatedDataset(self, request, context):
        """Deletes an annotated dataset by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LabelImage(self, request, context):
        """Starts a labeling task for image. The type of image labeling task is
    configured by feature in the request.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LabelVideo(self, request, context):
        """Starts a labeling task for video. The type of video labeling task is
    configured by feature in the request.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LabelText(self, request, context):
        """Starts a labeling task for text. The type of text labeling task is
    configured by feature in the request.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LabelAudio(self, request, context):
        """Starts a labeling task for audio. The type of audio labeling task is
    configured by feature in the request.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExample(self, request, context):
        """Gets an example by resource name, including both data and annotation.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListExamples(self, request, context):
        """Lists examples in an annotated dataset. Pagination is supported.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateAnnotationSpecSet(self, request, context):
        """Creates an annotation spec set by providing a set of labels.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAnnotationSpecSet(self, request, context):
        """Gets an annotation spec set by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListAnnotationSpecSets(self, request, context):
        """Lists annotation spec sets for a project. Pagination is supported.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteAnnotationSpecSet(self, request, context):
        """Deletes an annotation spec set by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateInstruction(self, request, context):
        """Creates an instruction for how data should be labeled.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetInstruction(self, request, context):
        """Gets an instruction by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListInstructions(self, request, context):
        """Lists instructions for a project. Pagination is supported.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteInstruction(self, request, context):
        """Deletes an instruction object by resource name.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DataLabelingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateDataset": grpc.unary_unary_rpc_method_handler(
            servicer.CreateDataset,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.CreateDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "GetDataset": grpc.unary_unary_rpc_method_handler(
            servicer.GetDataset,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "ListDatasets": grpc.unary_unary_rpc_method_handler(
            servicer.ListDatasets,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDatasetsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDatasetsResponse.SerializeToString,
        ),
        "DeleteDataset": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteDataset,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteDatasetRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ImportData": grpc.unary_unary_rpc_method_handler(
            servicer.ImportData,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ImportDataRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ExportData": grpc.unary_unary_rpc_method_handler(
            servicer.ExportData,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ExportDataRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetDataItem": grpc.unary_unary_rpc_method_handler(
            servicer.GetDataItem,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetDataItemRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.DataItem.SerializeToString,
        ),
        "ListDataItems": grpc.unary_unary_rpc_method_handler(
            servicer.ListDataItems,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDataItemsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListDataItemsResponse.SerializeToString,
        ),
        "GetAnnotatedDataset": grpc.unary_unary_rpc_method_handler(
            servicer.GetAnnotatedDataset,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetAnnotatedDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.AnnotatedDataset.SerializeToString,
        ),
        "ListAnnotatedDatasets": grpc.unary_unary_rpc_method_handler(
            servicer.ListAnnotatedDatasets,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotatedDatasetsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotatedDatasetsResponse.SerializeToString,
        ),
        "DeleteAnnotatedDataset": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAnnotatedDataset,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteAnnotatedDatasetRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "LabelImage": grpc.unary_unary_rpc_method_handler(
            servicer.LabelImage,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelImageRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "LabelVideo": grpc.unary_unary_rpc_method_handler(
            servicer.LabelVideo,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelVideoRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "LabelText": grpc.unary_unary_rpc_method_handler(
            servicer.LabelText,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelTextRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "LabelAudio": grpc.unary_unary_rpc_method_handler(
            servicer.LabelAudio,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.LabelAudioRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetExample": grpc.unary_unary_rpc_method_handler(
            servicer.GetExample,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetExampleRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.Example.SerializeToString,
        ),
        "ListExamples": grpc.unary_unary_rpc_method_handler(
            servicer.ListExamples,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListExamplesRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListExamplesResponse.SerializeToString,
        ),
        "CreateAnnotationSpecSet": grpc.unary_unary_rpc_method_handler(
            servicer.CreateAnnotationSpecSet,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.CreateAnnotationSpecSetRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_annotation__spec__set__pb2.AnnotationSpecSet.SerializeToString,
        ),
        "GetAnnotationSpecSet": grpc.unary_unary_rpc_method_handler(
            servicer.GetAnnotationSpecSet,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetAnnotationSpecSetRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_annotation__spec__set__pb2.AnnotationSpecSet.SerializeToString,
        ),
        "ListAnnotationSpecSets": grpc.unary_unary_rpc_method_handler(
            servicer.ListAnnotationSpecSets,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotationSpecSetsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListAnnotationSpecSetsResponse.SerializeToString,
        ),
        "DeleteAnnotationSpecSet": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAnnotationSpecSet,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteAnnotationSpecSetRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CreateInstruction": grpc.unary_unary_rpc_method_handler(
            servicer.CreateInstruction,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.CreateInstructionRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetInstruction": grpc.unary_unary_rpc_method_handler(
            servicer.GetInstruction,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.GetInstructionRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_instruction__pb2.Instruction.SerializeToString,
        ),
        "ListInstructions": grpc.unary_unary_rpc_method_handler(
            servicer.ListInstructions,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListInstructionsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.ListInstructionsResponse.SerializeToString,
        ),
        "DeleteInstruction": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteInstruction,
            request_deserializer=google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_data__labeling__service__pb2.DeleteInstructionRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.datalabeling.v1beta1.DataLabelingService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
