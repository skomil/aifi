/* tslint:disable */
/* eslint-disable */
/**
 * aifi - OpenAPI 3.0
 * ## Model Diagram ```mermaid classDiagram class Device {     string id     string label } class Rack {     string id     string label     string description     %% the below property is an array with cardinality [0..*]     string hiddenComponents } class UiSetting {     string id     string label     boolean hidden     string dataType     string uiType     object defaultValue     object initialValue } class DeviceFactory {     string id     string label     object apiConfiguration     string version }  class Asset {     string id     string type     string label     string description     string storageLocation     %% the below property is an array with cardinality [0..*]     string previewLocations }  class Rig {  } class Connection {     string id     string label     string description     string type     boolean required     boolean allowMultiple } class KeyValue {     string key     string value } class Error {     string message     integer code }  Rack \"1\" --> \"0..*\" Device : devices Rig \"1\" --> \"0..*\" DeviceFactory : factories Rig  \"1\" --> \"0..*\" KeyValue : config Rig  \"1\" --> \"0..*\" KeyValue : secrets DeviceFactory \"1\" --> \"0..1\"  Rack: rackAsDevice Rack \"1\" --> \"0..*\"  Connection: output Rig \"1\" --> \"0..*\" Rack : racks DeviceFactory \"1\" --> \"0..*\" Asset : assets Device \"1\" --> \"1\"  DeviceFactory: definition Device \"1\" --> \"0..*\"  UiSetting: uiSettingOverrides DeviceFactory \"1\" --> \"0..*\"  UiSetting: uiSettings DeviceFactory \"1\" --> \"0..*\"  Connection: input DeviceFactory \"1\" --> \"0..*\"  Connection: output ```
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export * from "./api";
export * from "./configuration";

