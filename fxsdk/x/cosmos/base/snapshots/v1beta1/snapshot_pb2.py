# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/snapshots/v1beta1/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,cosmos/base/snapshots/v1beta1/snapshot.proto\x12\x1d\x63osmos.base.snapshots.v1beta1\x1a\x14gogoproto/gogo.proto\"\x89\x01\n\x08Snapshot\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r\x12\x0e\n\x06\x63hunks\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12?\n\x08metadata\x18\x05 \x01(\x0b\x32\'.cosmos.base.snapshots.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\" \n\x08Metadata\x12\x14\n\x0c\x63hunk_hashes\x18\x01 \x03(\x0c\"\xcb\x03\n\x0cSnapshotItem\x12\x41\n\x05store\x18\x01 \x01(\x0b\x32\x30.cosmos.base.snapshots.v1beta1.SnapshotStoreItemH\x00\x12I\n\x04iavl\x18\x02 \x01(\x0b\x32/.cosmos.base.snapshots.v1beta1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x12I\n\textension\x18\x03 \x01(\x0b\x32\x34.cosmos.base.snapshots.v1beta1.SnapshotExtensionMetaH\x00\x12T\n\x11\x65xtension_payload\x18\x04 \x01(\x0b\x32\x37.cosmos.base.snapshots.v1beta1.SnapshotExtensionPayloadH\x00\x12\x43\n\x02kv\x18\x05 \x01(\x0b\x32-.cosmos.base.snapshots.v1beta1.SnapshotKVItemB\x06\xe2\xde\x1f\x02KVH\x00\x12?\n\x06schema\x18\x06 \x01(\x0b\x32-.cosmos.base.snapshots.v1beta1.SnapshotSchemaH\x00\x42\x06\n\x04item\"!\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05\"5\n\x15SnapshotExtensionMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r\"+\n\x18SnapshotExtensionPayload\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\",\n\x0eSnapshotKVItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x1e\n\x0eSnapshotSchema\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\x42.Z,github.com/cosmos/cosmos-sdk/snapshots/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.snapshots.v1beta1.snapshot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/snapshots/types'
  _SNAPSHOT.fields_by_name['metadata']._options = None
  _SNAPSHOT.fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _SNAPSHOTITEM.fields_by_name['iavl']._options = None
  _SNAPSHOTITEM.fields_by_name['iavl']._serialized_options = b'\342\336\037\004IAVL'
  _SNAPSHOTITEM.fields_by_name['kv']._options = None
  _SNAPSHOTITEM.fields_by_name['kv']._serialized_options = b'\342\336\037\002KV'
  _globals['_SNAPSHOT']._serialized_start=102
  _globals['_SNAPSHOT']._serialized_end=239
  _globals['_METADATA']._serialized_start=241
  _globals['_METADATA']._serialized_end=273
  _globals['_SNAPSHOTITEM']._serialized_start=276
  _globals['_SNAPSHOTITEM']._serialized_end=735
  _globals['_SNAPSHOTSTOREITEM']._serialized_start=737
  _globals['_SNAPSHOTSTOREITEM']._serialized_end=770
  _globals['_SNAPSHOTIAVLITEM']._serialized_start=772
  _globals['_SNAPSHOTIAVLITEM']._serialized_end=851
  _globals['_SNAPSHOTEXTENSIONMETA']._serialized_start=853
  _globals['_SNAPSHOTEXTENSIONMETA']._serialized_end=906
  _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_start=908
  _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_end=951
  _globals['_SNAPSHOTKVITEM']._serialized_start=953
  _globals['_SNAPSHOTKVITEM']._serialized_end=997
  _globals['_SNAPSHOTSCHEMA']._serialized_start=999
  _globals['_SNAPSHOTSCHEMA']._serialized_end=1029
# @@protoc_insertion_point(module_scope)
