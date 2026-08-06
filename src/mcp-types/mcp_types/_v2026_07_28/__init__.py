"""Internal wire-shape models for protocol 2026-07-28. Generated; do not edit.

Regenerate with `scripts/gen_surface_types.py` from `schema/2026-07-28.json`
(sha256 `6293cdfe015c14bd36eda4b1331ce37bda377609e58ed6d09d16f28e7d3c7ad4`)."""
# pyright: reportIncompatibleVariableOverride=false, reportGeneralTypeIssues=false

from __future__ import annotations

from typing import Any, Literal, Union

from dataclasses import dataclass


@dataclass(kw_only=True)
class BaseMetadata:
    """
    Base interface for metadata with name (identifier) and title (display name) properties.
    """

    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """


@dataclass(kw_only=True)
class BooleanSchema:
    default: bool | None = None
    description: str | None = None
    title: str | None = None
    type: Literal["boolean"]


@dataclass(kw_only=True)
class Argument:
    """
    The argument's information
    """

    name: str
    """
    The name of the argument
    """
    value: str
    """
    The value of the argument to use for completion matching.
    """


@dataclass(kw_only=True)
class Context:
    """
    Additional, optional context for completions
    """

    arguments: dict[str, str] | None = None
    """
    Previously-resolved variables in a URI template or prompt.
    """


@dataclass(kw_only=True)
class Completion:
    has_more: bool | None = None
    """
    Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown.
    """
    total: int | None = None
    """
    The total number of completion options available. This can exceed the number of values actually sent in the response.
    """
    values: list[str]
    """
    An array of completion values. Must not exceed 100 items.
    """


@dataclass(kw_only=True)
class Cursor:
    root: str
    """
    An opaque token used to represent a cursor for pagination.
    """


@dataclass(kw_only=True)
class RequestedSchema:
    """
    A restricted subset of JSON Schema.
    Only top-level properties are allowed, without nesting.
    """

    schema_: str | None = None
    properties: dict[str, Any]
    required: list[str] | None = None
    type: Literal["object"]


@dataclass(kw_only=True)
class ElicitRequestFormParams:
    """
    The parameters for a request to elicit non-sensitive information from the user via a form in the client.
    """

    message: str
    """
    The message to present to the user describing what information is being requested.
    """
    mode: Literal["form"] = "form"
    """
    The elicitation mode.
    """
    requested_schema: RequestedSchema
    """
    A restricted subset of JSON Schema.
    Only top-level properties are allowed, without nesting.
    """


@dataclass(kw_only=True)
class ElicitRequestURLParams:
    """
    The parameters for a request to elicit information from the user via a URL in the client.
    """

    message: str
    """
    The message to present to the user explaining why the interaction is needed.
    """
    mode: Literal["url"]
    """
    The elicitation mode.
    """
    url: str
    """
    The URL that the user should navigate to.
    """


@dataclass(kw_only=True)
class ElicitResult:
    """
    The result returned by the client for an {@link ElicitRequestelicitation/create} request.
    """

    action: Literal["accept", "cancel", "decline"]
    """
    The user action in response to the elicitation.
    - `"accept"`: User submitted the form/confirmed the action
    - `"decline"`: User explicitly declined the action
    - `"cancel"`: User dismissed without making an explicit choice
    """
    content: dict[str, list[str] | str | int | float | bool | None] | None = None
    """
    The submitted form data, only present when action is `"accept"` and mode was `"form"`.
    Contains values matching the requested schema.
    Omitted for out-of-band mode responses.
    """


@dataclass(kw_only=True)
class Error:
    code: int
    """
    The error type that occurred.
    """
    data: Any | None = None
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """
    message: str
    """
    A short description of the error. The message SHOULD be limited to a concise single sentence.
    """


@dataclass(kw_only=True)
class Error1(Error):
    code: Literal[-32020]
    """
    The error type that occurred.
    """


@dataclass(kw_only=True)
class Icon:
    """
    An optionally-sized icon that can be displayed in a user interface.
    """

    mime_type: str | None = None
    """
    Optional MIME type override if the source MIME type is missing or generic.
    For example: `"image/png"`, `"image/jpeg"`, or `"image/svg+xml"`.
    """
    sizes: list[str] | None = None
    """
    Optional array of strings that specify sizes at which the icon can be used.
    Each string should be in WxH format (e.g., `"48x48"`, `"96x96"`) or `"any"` for scalable formats like SVG.

    If not provided, the client should assume that the icon can be used at any size.
    """
    src: str
    """
    A standard URI pointing to an icon resource. May be an HTTP/HTTPS URL or a
    `data:` URI with Base64-encoded image data.

    Consumers SHOULD take steps to ensure URLs serving icons are from the
    same domain as the client/server or a trusted domain.

    Consumers SHOULD take appropriate precautions when consuming SVGs as they can contain
    executable JavaScript.
    """
    theme: Literal["dark", "light"] | None = None
    """
    Optional specifier for the theme this icon is designed for. `"light"` indicates
    the icon is designed to be used with a light background, and `"dark"` indicates
    the icon is designed to be used with a dark background.

    If not provided, the client should assume the icon can be used with any theme.
    """


@dataclass(kw_only=True)
class Icons:
    """
    Base interface to add `icons` property.
    """

    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """


@dataclass(kw_only=True)
class Implementation:
    """
    Describes the MCP implementation.
    """

    description: str | None = None
    """
    An optional human-readable description of what this implementation does.

    This can be used by clients or servers to provide context about their purpose
    and capabilities. For example, a server might describe the types of resources
    or tools it provides, while a client might describe its intended use case.
    """
    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """
    version: str
    """
    The version of this implementation.
    """
    website_url: str | None = None
    """
    An optional URL of the website for this implementation.
    """


@dataclass(kw_only=True)
class InternalError:
    """
    A JSON-RPC error indicating that an internal error occurred on the receiver. This error is returned when the receiver encounters an unexpected condition that prevents it from fulfilling the request.
    """

    code: Literal[-32603]
    """
    The error type that occurred.
    """
    data: Any | None = None
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """
    message: str
    """
    A short description of the error. The message SHOULD be limited to a concise single sentence.
    """


@dataclass(kw_only=True)
class InvalidParamsError:
    """
    A JSON-RPC error indicating that the method parameters are invalid or malformed.

    In MCP, this error is returned in various contexts when request parameters fail validation:

    - **Tools**: Unknown tool name or invalid tool arguments
    - **Prompts**: Unknown prompt name or missing required arguments
    - **Pagination**: Invalid or expired cursor values
    - **Logging**: Invalid log level
    - **Elicitation**: Server requests an elicitation mode not declared in client capabilities
    - **Sampling**: Missing tool result or tool results mixed with other content
    """

    code: Literal[-32602]
    """
    The error type that occurred.
    """
    data: Any | None = None
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """
    message: str
    """
    A short description of the error. The message SHOULD be limited to a concise single sentence.
    """


@dataclass(kw_only=True)
class InvalidRequestError:
    """
    A JSON-RPC error indicating that the request is not a valid request object. This error is returned when the message structure does not conform to the JSON-RPC 2.0 specification requirements for a request (e.g., missing required fields like `jsonrpc` or `method`, or using invalid types for these fields).
    """

    code: Literal[-32600]
    """
    The error type that occurred.
    """
    data: Any | None = None
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """
    message: str
    """
    A short description of the error. The message SHOULD be limited to a concise single sentence.
    """


@dataclass(kw_only=True)
class JSONRPCNotification:
    """
    A notification which does not expect a response.
    """

    jsonrpc: Literal["2.0"]
    method: str
    params: dict[str, Any] | None = None


@dataclass(kw_only=True)
class LegacyTitledEnumSchema:
    """
    Use {@link TitledSingleSelectEnumSchema} instead.
    This interface will be removed in a future version.
    """

    default: str | None = None
    description: str | None = None
    enum: list[str]
    enum_names: list[str] | None = None
    """
    (Legacy) Display names for enum values.
    Non-standard according to JSON schema 2020-12.
    """
    title: str | None = None
    type: Literal["string"]


@dataclass(kw_only=True)
class LoggingLevel:
    root: Literal["alert", "critical", "debug", "emergency", "error", "info", "notice", "warning"]
    """
    The severity of a log message.

    These map to syslog message severities, as specified in RFC-5424:
    https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1
    """


@dataclass(kw_only=True)
class MetaObject:
    """
    Represents the contents of a `_meta` field, which clients and servers use to attach additional metadata to their interactions.

    Certain key names are reserved by MCP for protocol-level metadata; implementations MUST NOT make assumptions about values at these keys. Additionally, specific schema definitions may reserve particular names for purpose-specific metadata, as declared in those definitions.

    Valid keys have two segments:

    **Prefix:**
    - Optional — if specified, MUST be a series of _labels_ separated by dots (`.`), followed by a slash (`/`).
    - Labels MUST start with a letter and end with a letter or digit. Interior characters may be letters, digits, or hyphens (`-`).
    - Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`).
    - Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use. For example: `io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved. However, `com.example.mcp/` is NOT reserved, as the second label is `example`.

    **Name:**
    - Unless empty, MUST start and end with an alphanumeric character (`[a-z0-9A-Z]`).
    - Interior characters may be alphanumeric, hyphens (`-`), underscores (`_`), or dots (`.`).
    """


@dataclass(kw_only=True)
class MethodNotFoundError:
    """
    A JSON-RPC error indicating that the requested method does not exist or is not available.

    In MCP, a server returns this error when a client invokes a method the server does not implement — either a genuinely unknown method, or one gated behind a server capability the server did not advertise (e.g., calling `prompts/list` when the `prompts` capability was not advertised).

    A request that requires a client capability the client did not declare is signalled instead by {@link MissingRequiredClientCapabilityError} (`-32021`).
    """

    code: Literal[-32601]
    """
    The error type that occurred.
    """
    data: Any | None = None
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """
    message: str
    """
    A short description of the error. The message SHOULD be limited to a concise single sentence.
    """


@dataclass(kw_only=True)
class ModelHint:
    """
    Hints to use for model selection.

    Keys not declared here are currently left unspecified by the spec and are up
    to the client to interpret.
    """

    name: str | None = None
    """
    A hint for a model name.

    The client SHOULD treat this as a substring of a model name; for example:
     - `claude-3-5-sonnet` should match `claude-3-5-sonnet-20241022`
     - `sonnet` should match `claude-3-5-sonnet-20241022`, `claude-3-sonnet-20240229`, etc.
     - `claude` should match any Claude model

    The client MAY also map the string to a different provider's model name or a different model family, as long as it fills a similar niche; for example:
     - `gemini-1.5-flash` could match `claude-3-haiku-20240307`
    """


@dataclass(kw_only=True)
class ModelPreferences:
    """
    The server's preferences for model selection, requested of the client during sampling.

    Because LLMs can vary along multiple dimensions, choosing the "best" model is
    rarely straightforward.  Different models excel in different areas—some are
    faster but less capable, others are more capable but more expensive, and so
    on. This interface allows servers to express their priorities across multiple
    dimensions to help clients make an appropriate selection for their use case.

    These preferences are always advisory. The client MAY ignore them. It is also
    up to the client to decide how to interpret these preferences and how to
    balance them against other considerations.
    """

    cost_priority: float | None = None
    """
    How much to prioritize cost when selecting a model. A value of 0 means cost
    is not important, while a value of 1 means cost is the most important
    factor.
    """
    hints: list[ModelHint] | None = None
    """
    Optional hints to use for model selection.

    If multiple hints are specified, the client MUST evaluate them in order
    (such that the first match is taken).

    The client SHOULD prioritize these hints over the numeric priorities, but
    MAY still use the priorities to select from ambiguous matches.
    """
    intelligence_priority: float | None = None
    """
    How much to prioritize intelligence and capabilities when selecting a
    model. A value of 0 means intelligence is not important, while a value of 1
    means intelligence is the most important factor.
    """
    speed_priority: float | None = None
    """
    How much to prioritize sampling speed (latency) when selecting a model. A
    value of 0 means speed is not important, while a value of 1 means speed is
    the most important factor.
    """


@dataclass(kw_only=True)
class Notification:
    method: str
    params: dict[str, Any] | None = None


@dataclass(kw_only=True)
class NumberSchema:
    default: int | float | None = None
    description: str | None = None
    maximum: int | float | None = None
    minimum: int | float | None = None
    title: str | None = None
    type: Literal["integer", "number"]


@dataclass(kw_only=True)
class ParseError:
    """
    A JSON-RPC error indicating that invalid JSON was received by the server. This error is returned when the server cannot parse the JSON text of a message.
    """

    code: Literal[-32700]
    """
    The error type that occurred.
    """
    data: Any | None = None
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """
    message: str
    """
    A short description of the error. The message SHOULD be limited to a concise single sentence.
    """


@dataclass(kw_only=True)
class ProgressToken:
    root: str | int
    """
    A progress token, used to associate progress notifications with the original request.
    """


@dataclass(kw_only=True)
class PromptArgument:
    """
    Describes an argument that a prompt can accept.
    """

    description: str | None = None
    """
    A human-readable description of the argument.
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    required: bool | None = None
    """
    Whether this argument must be provided.
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """


@dataclass(kw_only=True)
class PromptReference:
    """
    Identifies a prompt.
    """

    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """
    type: Literal["ref/prompt"]


@dataclass(kw_only=True)
class Request:
    method: str
    params: dict[str, Any] | None = None


@dataclass(kw_only=True)
class RequestId:
    root: str | int
    """
    A uniquely identifying ID for a request in JSON-RPC.
    """


@dataclass(kw_only=True)
class ResourceContents:
    """
    The contents of a specific resource or sub-resource.
    """

    meta: MetaObject | None = None
    mime_type: str | None = None
    """
    The MIME type of this resource, if known.
    """
    uri: str
    """
    The URI of this resource.
    """


@dataclass(kw_only=True)
class ResourceTemplateReference:
    """
    A reference to a resource or resource template definition.
    """

    type: Literal["ref/resource"]
    uri: str
    """
    The URI or URI template of the resource.
    """


@dataclass(kw_only=True)
class ResultMetaObject:
    """
    Extends {@link MetaObject} with additional result-specific fields. All key naming rules from `MetaObject` apply.
    """

    io_modelcontextprotocol_server_info: Any | None = None
    """
    Identifies the server software producing the response. Servers SHOULD
    include this field on every response unless specifically configured not
    to do so.

    The {@link Implementation} schema requires `name` and `version`; other
    fields are optional.

    The value is self-reported by the server and is not verified by the
    protocol. It is intended for display, logging, and debugging. Clients
    SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
    security decisions.
    """


@dataclass(kw_only=True)
class ResultType:
    root: str
    """
    Indicates the type of a {@link Result} object, allowing the client to
    determine how to parse the response.

    complete - the request completed successfully and the result contains the final content.
    input_required - the request requires additional input and the result contains an {@link InputRequiredResult} object with instructions for the client to provide additional input before retrying the original request.
    """


@dataclass(kw_only=True)
class Role:
    root: Literal["assistant", "user"]
    """
    The sender or recipient of messages and data in a conversation.
    """


@dataclass(kw_only=True)
class Root:
    """
    Represents a root directory or file that the server can operate on.
    """

    meta: MetaObject | None = None
    name: str | None = None
    """
    An optional name for the root. This can be used to provide a human-readable
    identifier for the root, which may be useful for display purposes or for
    referencing the root in other parts of the application.
    """
    uri: str
    """
    The URI identifying the root. This *must* start with `file://` for now.
    This restriction may be relaxed in future versions of the protocol to allow
    other URI schemes.
    """


@dataclass(kw_only=True)
class Prompts:
    """
    Present if the server offers any prompt templates.
    """

    list_changed: bool | None = None
    """
    Whether this server supports notifications for changes to the prompt list.
    """


@dataclass(kw_only=True)
class Resources:
    """
    Present if the server offers any resources to read.
    """

    list_changed: bool | None = None
    """
    Whether this server supports notifications for changes to the resource list.
    """
    subscribe: bool | None = None
    """
    Whether this server supports subscribing to resource updates.
    """


@dataclass(kw_only=True)
class Tools:
    """
    Present if the server offers any tools to call.
    """

    list_changed: bool | None = None
    """
    Whether this server supports notifications for changes to the tool list.
    """


@dataclass(kw_only=True)
class StringSchema:
    default: str | None = None
    description: str | None = None
    format: Literal["date", "date-time", "email", "uri"] | None = None
    max_length: int | None = None
    min_length: int | None = None
    title: str | None = None
    type: Literal["string"]


@dataclass(kw_only=True)
class SubscriptionFilter:
    """
    The set of notification types a client may opt in to on a
    {@link SubscriptionsListenRequestsubscriptions/listen} request.

    Each notification type is **opt-in**; the server **MUST NOT** send
    notification types the client has not explicitly requested here.
    """

    prompts_list_changed: bool | None = None
    """
    If true, receive {@link PromptListChangedNotificationnotifications/prompts/list_changed}.
    """
    resource_subscriptions: list[str] | None = None
    """
    Subscribe to {@link ResourceUpdatedNotificationnotifications/resources/updated} for these resource URIs.
    Replaces the former `resources/subscribe` RPC.
    """
    resources_list_changed: bool | None = None
    """
    If true, receive {@link ResourceListChangedNotificationnotifications/resources/list_changed}.
    """
    tools_list_changed: bool | None = None
    """
    If true, receive {@link ToolListChangedNotificationnotifications/tools/list_changed}.
    """


@dataclass(kw_only=True)
class SubscriptionsListenResultMeta:
    """
    Extends {@link ResultMetaObject} with the subscription-stream identifier carried by a
    {@link SubscriptionsListenResult}. All key naming rules from `MetaObject` apply.
    """

    io_modelcontextprotocol_server_info: Any | None = None
    """
    Identifies the server software producing the response. Servers SHOULD
    include this field on every response unless specifically configured not
    to do so.

    The {@link Implementation} schema requires `name` and `version`; other
    fields are optional.

    The value is self-reported by the server and is not verified by the
    protocol. It is intended for display, logging, and debugging. Clients
    SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
    security decisions.
    """
    io_modelcontextprotocol_subscription_id: RequestId
    """
    Identifies the subscription stream this response closes, so the client can
    correlate it with the originating subscription — mirroring the same key on
    the stream's notifications. The value is the JSON-RPC ID of the
    `subscriptions/listen` request that opened the stream (and equals this
    response's `id`).
    """


@dataclass(kw_only=True)
class TextResourceContents:
    meta: MetaObject | None = None
    mime_type: str | None = None
    """
    The MIME type of this resource, if known.
    """
    text: str
    """
    The text of the item. This must only be set if the item can actually be represented as text (not binary data).
    """
    uri: str
    """
    The URI of this resource.
    """


@dataclass(kw_only=True)
class AnyOfItem:
    const: str
    """
    The constant enum value.
    """
    title: str
    """
    Display title for this option.
    """


@dataclass(kw_only=True)
class Items:
    """
    Schema for array items with enum options and display labels.
    """

    any_of: list[AnyOfItem]
    """
    Array of enum options with values and display labels.
    """


@dataclass(kw_only=True)
class TitledMultiSelectEnumSchema:
    """
    Schema for multiple-selection enumeration with display titles for each option.
    """

    default: list[str] | None = None
    """
    Optional default value.
    """
    description: str | None = None
    """
    Optional description for the enum field.
    """
    items: Items
    """
    Schema for array items with enum options and display labels.
    """
    max_items: int | None = None
    """
    Maximum number of items to select.
    """
    min_items: int | None = None
    """
    Minimum number of items to select.
    """
    title: str | None = None
    """
    Optional title for the enum field.
    """
    type: Literal["array"]


@dataclass(kw_only=True)
class OneOfItem:
    const: str
    """
    The enum value.
    """
    title: str
    """
    Display label for this option.
    """


@dataclass(kw_only=True)
class TitledSingleSelectEnumSchema:
    """
    Schema for single-selection enumeration with display titles for each option.
    """

    default: str | None = None
    """
    Optional default value.
    """
    description: str | None = None
    """
    Optional description for the enum field.
    """
    one_of: list[OneOfItem]
    """
    Array of enum options with values and display labels.
    """
    title: str | None = None
    """
    Optional title for the enum field.
    """
    type: Literal["string"]


@dataclass(kw_only=True)
class InputSchema:
    """
    A JSON Schema object defining the expected parameters for the tool.

    Tool arguments are always JSON objects, so `type: "object"` is required at the root.
    Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — including
    composition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords
    (`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any other
    standard validation or annotation keywords.

    Property schemas may carry an `x-mcp-header` annotation to mirror the
    argument value into an HTTP header on the Streamable HTTP transport. See
    the Streamable HTTP transport specification for the validity and
    extraction rules.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """

    schema_: str | None = None
    type: Literal["object"]


@dataclass(kw_only=True)
class OutputSchema:
    """
    An optional JSON Schema object defining the structure of the tool's output returned in
    the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """

    schema_: str | None = None


@dataclass(kw_only=True)
class ToolAnnotations:
    """
    Additional properties describing a {@link Tool} to clients.

    NOTE: all properties in `ToolAnnotations` are **hints**.
    They are not guaranteed to provide a faithful description of
    tool behavior (including descriptive properties like `title`).

    Clients should never make tool use decisions based on `ToolAnnotations`
    received from untrusted servers.
    """

    destructive_hint: bool | None = None
    """
    If true, the tool may perform destructive updates to its environment.
    If false, the tool performs only additive updates.

    (This property is meaningful only when `readOnlyHint == false`)

    Default: true
    """
    idempotent_hint: bool | None = None
    """
    If true, calling the tool repeatedly with the same arguments
    will have no additional effect on its environment.

    (This property is meaningful only when `readOnlyHint == false`)

    Default: false
    """
    open_world_hint: bool | None = None
    """
    If true, this tool may interact with an "open world" of external
    entities. If false, the tool's domain of interaction is closed.
    For example, the world of a web search tool is open, whereas that
    of a memory tool is not.

    Default: true
    """
    read_only_hint: bool | None = None
    """
    If true, the tool does not modify its environment.

    Default: false
    """
    title: str | None = None
    """
    A human-readable title for the tool.
    """


@dataclass(kw_only=True)
class ToolChoice:
    """
    Controls tool selection behavior for sampling requests.
    """

    mode: Literal["auto", "none", "required"] | None = None
    """
    Controls the tool use ability of the model:
    - `"auto"`: Model decides whether to use tools (default)
    - `"required"`: Model MUST use at least one tool before completing
    - `"none"`: Model MUST NOT use any tools
    """


@dataclass(kw_only=True)
class ToolUseContent:
    """
    A request from the assistant to call a tool.
    """

    meta: MetaObject | None = None
    """
    Optional metadata about the tool use. Clients SHOULD preserve this field when
    including tool uses in subsequent sampling requests to enable caching optimizations.
    """
    id: str
    """
    A unique identifier for this tool use.

    This ID is used to match tool results to their corresponding tool uses.
    """
    input: dict[str, Any]
    """
    The arguments to pass to the tool, conforming to the tool's input schema.
    """
    name: str
    """
    The name of the tool to call.
    """
    type: Literal["tool_use"]


@dataclass(kw_only=True)
class Data1:
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """

    requested: str
    """
    The protocol version that was requested by the client.
    """
    supported: list[str]
    """
    Protocol versions the server supports. The client should choose a
    mutually supported version from this list and retry.
    """


@dataclass(kw_only=True)
class Error3(Error):
    code: Literal[-32022]
    """
    The error type that occurred.
    """
    data: Data1
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """


@dataclass(kw_only=True)
class UnsupportedProtocolVersionError:
    """
    Returned when the request's protocol version is unknown to the server or
    unsupported (e.g., a known experimental or draft version the server has
    chosen not to implement). For HTTP, the response status code MUST be
    `400 Bad Request`.
    """

    error: Error3
    id: RequestId | None = None
    jsonrpc: Literal["2.0"]


@dataclass(kw_only=True)
class Items1:
    """
    Schema for the array items.
    """

    enum: list[str]
    """
    Array of enum values to choose from.
    """
    type: Literal["string"]


@dataclass(kw_only=True)
class UntitledMultiSelectEnumSchema:
    """
    Schema for multiple-selection enumeration without display titles for options.
    """

    default: list[str] | None = None
    """
    Optional default value.
    """
    description: str | None = None
    """
    Optional description for the enum field.
    """
    items: Items1
    """
    Schema for the array items.
    """
    max_items: int | None = None
    """
    Maximum number of items to select.
    """
    min_items: int | None = None
    """
    Minimum number of items to select.
    """
    title: str | None = None
    """
    Optional title for the enum field.
    """
    type: Literal["array"]


@dataclass(kw_only=True)
class UntitledSingleSelectEnumSchema:
    """
    Schema for single-selection enumeration without display titles for options.
    """

    default: str | None = None
    """
    Optional default value.
    """
    description: str | None = None
    """
    Optional description for the enum field.
    """
    enum: list[str]
    """
    Array of enum values to choose from.
    """
    title: str | None = None
    """
    Optional title for the enum field.
    """
    type: Literal["string"]


@dataclass(kw_only=True)
class Annotations:
    """
    Optional annotations for the client. The client can use annotations to inform how objects are used or displayed
    """

    audience: list[Role] | None = None
    """
    Describes who the intended audience of this object or data is.

    It can include multiple entries to indicate content useful for multiple audiences (e.g., `["user", "assistant"]`).
    """
    last_modified: str | None = None
    """
    The moment the resource was last modified, as an ISO 8601 formatted string.

    Should be an ISO 8601 formatted string (e.g., "2025-01-12T15:00:58Z").

    Examples: last activity timestamp in an open file, timestamp when the resource
    was attached, etc.
    """
    priority: float | None = None
    """
    Describes how important this data is for operating the server.

    A value of 1 means "most important," and indicates that the data is
    effectively required, while 0 means "least important," and indicates that
    the data is entirely optional.
    """


@dataclass(kw_only=True)
class AudioContent:
    """
    Audio provided to or from an LLM.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    data: str
    """
    The base64-encoded audio data.
    """
    mime_type: str
    """
    The MIME type of the audio. Different providers may support different audio types.
    """
    type: Literal["audio"]


@dataclass(kw_only=True)
class BlobResourceContents:
    meta: MetaObject | None = None
    blob: str
    """
    A base64-encoded string representing the binary data of the item.
    """
    mime_type: str | None = None
    """
    The MIME type of this resource, if known.
    """
    uri: str
    """
    The URI of this resource.
    """


@dataclass(kw_only=True)
class CacheableResult:
    """
    A result that supports a time-to-live (TTL) hint for client-side caching.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class CompleteResult:
    """
    The result returned by the server for a {@link CompleteRequestcompletion/complete} request.
    """

    meta: ResultMetaObject | None = None
    completion: Completion
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """


@dataclass(kw_only=True)
class CompleteResultResponse:
    """
    A successful response from the server for a {@link CompleteRequestcompletion/complete} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: CompleteResult


@dataclass(kw_only=True)
class ElicitRequestParams:
    root: ElicitRequestFormParams | ElicitRequestURLParams
    """
    The parameters for a request to elicit additional information from the user via the client.
    """


@dataclass(kw_only=True)
class EmbeddedResource:
    """
    The contents of a resource, embedded into a prompt or tool call result.

    It is up to the client how best to render embedded resources for the benefit
    of the LLM and/or the user.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    resource: TextResourceContents | BlobResourceContents
    type: Literal["resource"]


@dataclass(kw_only=True)
class EnumSchema:
    root: (
        UntitledSingleSelectEnumSchema
        | TitledSingleSelectEnumSchema
        | UntitledMultiSelectEnumSchema
        | TitledMultiSelectEnumSchema
        | LegacyTitledEnumSchema
    )


@dataclass(kw_only=True)
class HeaderMismatchError:
    """
    Returned when a server rejects a request because the values in the HTTP
    headers do not match the corresponding values in the request body, or
    because required headers are missing or malformed. For HTTP, the response
    status code MUST be `400 Bad Request`.
    """

    error: Error1
    id: RequestId | None = None
    jsonrpc: Literal["2.0"]


@dataclass(kw_only=True)
class ImageContent:
    """
    An image provided to or from an LLM.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    data: str
    """
    The base64-encoded image data.
    """
    mime_type: str
    """
    The MIME type of the image. Different providers may support different image types.
    """
    type: Literal["image"]


@dataclass(kw_only=True)
class JSONRPCErrorResponse:
    """
    A response to a request that indicates an error occurred.
    """

    error: Error
    id: RequestId | None = None
    jsonrpc: Literal["2.0"]


@dataclass(kw_only=True)
class JSONRPCRequest:
    """
    A request that expects a response.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: str
    params: dict[str, Any] | None = None


@dataclass(kw_only=True)
class Params:
    meta: MetaObject | None = None


@dataclass(kw_only=True)
class ListRootsRequest:
    """
    Sent from the server to request a list of root URIs from the client. Roots allow
    servers to ask for specific directories or files to operate on. A common example
    for roots is providing a set of repositories or directories a server should operate
    on.

    This request is typically used when the server needs to understand the file system
    structure or access specific locations that the client has permission to read from.
    """

    method: Literal["roots/list"]
    params: Params | None = None


@dataclass(kw_only=True)
class ListRootsResult:
    """
    The result returned by the client for a {@link ListRootsRequestroots/list} request.
    This result contains an array of {@link Root} objects, each representing a root directory
    or file that the server can operate on.
    """

    roots: list[Root]


@dataclass(kw_only=True)
class MultiSelectEnumSchema:
    root: UntitledMultiSelectEnumSchema | TitledMultiSelectEnumSchema


@dataclass(kw_only=True)
class NotificationMetaObject:
    """
    Extends {@link MetaObject} with additional notification-specific fields. All key naming rules from `MetaObject` apply.
    """

    io_modelcontextprotocol_subscription_id: RequestId | None = None
    """
    Identifies the subscription stream a notification was delivered on. The
    server MUST include this key on every notification delivered via a
    {@link SubscriptionsListenRequestsubscriptions/listen} stream, so the
    client can correlate the notification with the originating subscription.
    The key is absent on notifications not delivered via a subscription
    stream (e.g. progress notifications for an in-flight request), which is
    why it is optional here.

    The value is the JSON-RPC ID of the `subscriptions/listen` request that
    opened the stream.
    """


@dataclass(kw_only=True)
class NotificationParams:
    """
    Common params for any notification.
    """

    meta: NotificationMetaObject | None = None


@dataclass(kw_only=True)
class PaginatedResult:
    meta: ResultMetaObject | None = None
    next_cursor: str | None = None
    """
    An opaque token representing the pagination position after the last returned result.
    If present, there may be more results available.
    """
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """


@dataclass(kw_only=True)
class PrimitiveSchemaDefinition:
    root: (
        StringSchema
        | NumberSchema
        | BooleanSchema
        | UntitledSingleSelectEnumSchema
        | TitledSingleSelectEnumSchema
        | UntitledMultiSelectEnumSchema
        | TitledMultiSelectEnumSchema
        | LegacyTitledEnumSchema
    )
    """
    Restricted schema definitions that only allow primitive types
    without nested objects or arrays.
    """


@dataclass(kw_only=True)
class ProgressNotificationParams:
    """
    Parameters for a {@link ProgressNotificationnotifications/progress} notification.
    """

    meta: NotificationMetaObject | None = None
    message: str | None = None
    """
    An optional message describing the current progress.
    """
    progress: float
    """
    The progress thus far. This should increase every time progress is made, even if the total is unknown.
    """
    progress_token: ProgressToken
    """
    The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.
    """
    total: float | None = None
    """
    Total number of items to process (or total progress required), if known.
    """


@dataclass(kw_only=True)
class Prompt:
    """
    A prompt or prompt template that the server offers.
    """

    meta: MetaObject | None = None
    arguments: list[PromptArgument] | None = None
    """
    A list of arguments to use for templating the prompt.
    """
    description: str | None = None
    """
    An optional description of what this prompt provides
    """
    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """


@dataclass(kw_only=True)
class PromptListChangedNotification:
    """
    An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `promptsListChanged` filter field.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/prompts/list_changed"]
    params: NotificationParams | None = None


@dataclass(kw_only=True)
class ReadResourceResult:
    """
    The result returned by the server for a {@link ReadResourceRequestresources/read} request.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    contents: list[TextResourceContents | BlobResourceContents]
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class Resource:
    """
    A known resource that the server is capable of reading.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    description: str | None = None
    """
    A description of what this resource represents.

    This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.
    """
    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """
    mime_type: str | None = None
    """
    The MIME type of this resource, if known.
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    size: int | None = None
    """
    The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

    This can be used by Hosts to display file sizes and estimate context window usage.
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """
    uri: str
    """
    The URI of this resource.
    """


@dataclass(kw_only=True)
class ResourceLink:
    """
    A resource that the server is capable of reading, included in a prompt or tool call result.

    Note: resource links returned by tools are not guaranteed to appear in the results of {@link ListResourcesRequestresources/list} requests.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    description: str | None = None
    """
    A description of what this resource represents.

    This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.
    """
    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """
    mime_type: str | None = None
    """
    The MIME type of this resource, if known.
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    size: int | None = None
    """
    The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

    This can be used by Hosts to display file sizes and estimate context window usage.
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """
    type: Literal["resource_link"]
    uri: str
    """
    The URI of this resource.
    """


@dataclass(kw_only=True)
class ResourceListChangedNotification:
    """
    An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `resourcesListChanged` filter field.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/resources/list_changed"]
    params: NotificationParams | None = None


@dataclass(kw_only=True)
class ResourceTemplate:
    """
    A template description for resources available on the server.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    description: str | None = None
    """
    A description of what this template is for.

    This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.
    """
    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """
    mime_type: str | None = None
    """
    The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type.
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """
    uri_template: str
    """
    A URI template (according to RFC 6570) that can be used to construct resource URIs.
    """


@dataclass(kw_only=True)
class ResourceUpdatedNotificationParams:
    """
    Parameters for a `notifications/resources/updated` notification.
    """

    meta: NotificationMetaObject | None = None
    uri: str
    """
    The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to.
    """


@dataclass(kw_only=True)
class Result:
    """
    Common result fields.
    """

    meta: ResultMetaObject | None = None
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """


@dataclass(kw_only=True)
class SingleSelectEnumSchema:
    root: UntitledSingleSelectEnumSchema | TitledSingleSelectEnumSchema


@dataclass(kw_only=True)
class SubscriptionsAcknowledgedNotificationParams:
    """
    Parameters for a {@link SubscriptionsAcknowledgedNotificationnotifications/subscriptions/acknowledged} notification.
    """

    meta: NotificationMetaObject | None = None
    notifications: SubscriptionFilter
    """
    The subset of requested notification types the server agreed to honor.
    Only includes notification types the server actually supports; if the
    client requested an unsupported type (e.g., `promptsListChanged` when
    the server has no prompts), it is omitted from this set.
    """


@dataclass(kw_only=True)
class SubscriptionsListenResult:
    """
    The response to a {@link SubscriptionsListenRequestsubscriptions/listen}
    request, signalling that the subscription has ended gracefully (for example,
    during server shutdown). Because the listen stream is long-lived, this result
    is sent only when the server tears the subscription down; an abrupt transport
    close carries no response. The result body is otherwise empty.
    """

    meta: SubscriptionsListenResultMeta
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """


@dataclass(kw_only=True)
class TextContent:
    """
    Text provided to or from an LLM.
    """

    meta: MetaObject | None = None
    annotations: Annotations | None = None
    """
    Optional annotations for the client.
    """
    text: str
    """
    The text content of the message.
    """
    type: Literal["text"]


@dataclass(kw_only=True)
class Tool:
    """
    Definition for a tool the client can call.
    """

    meta: MetaObject | None = None
    annotations: ToolAnnotations | None = None
    """
    Optional additional tool information.

    Display name precedence order is: `title`, `annotations.title`, then `name`.
    """
    description: str | None = None
    """
    A human-readable description of the tool.

    This can be used by clients to improve the LLM's understanding of available tools. It can be thought of like a "hint" to the model.
    """
    icons: list[Icon] | None = None
    """
    Optional set of sized icons that the client can display in a user interface.

    Clients that support rendering icons MUST support at least the following MIME types:
    - `image/png` - PNG images (safe, universal compatibility)
    - `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

    Clients that support rendering icons SHOULD also support:
    - `image/svg+xml` - SVG images (scalable but requires security precautions)
    - `image/webp` - WebP images (modern, efficient format)
    """
    input_schema: InputSchema
    """
    A JSON Schema object defining the expected parameters for the tool.

    Tool arguments are always JSON objects, so `type: "object"` is required at the root.
    Beyond that, any JSON Schema 2020-12 keyword may appear alongside `type` — including
    composition keywords (`oneOf`, `anyOf`, `allOf`, `not`), conditional keywords
    (`if`/`then`/`else`), reference keywords (`$ref`, `$defs`, `$anchor`), and any other
    standard validation or annotation keywords.

    Property schemas may carry an `x-mcp-header` annotation to mirror the
    argument value into an HTTP header on the Streamable HTTP transport. See
    the Streamable HTTP transport specification for the validity and
    extraction rules.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """
    name: str
    """
    Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).
    """
    output_schema: OutputSchema | None = None
    """
    An optional JSON Schema object defining the structure of the tool's output returned in
    the structuredContent field of a {@link CallToolResult}. This can be any valid JSON Schema 2020-12.

    Defaults to JSON Schema 2020-12 when no explicit `$schema` is provided.
    """
    title: str | None = None
    """
    Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
    even by those unfamiliar with domain-specific terminology.

    If not provided, the name should be used for display (except for {@link Tool},
    where `annotations.title` should be given precedence over using `name`,
    if present).
    """


@dataclass(kw_only=True)
class ToolListChangedNotification:
    """
    An optional notification from the server to the client, informing it that the list of tools it offers has changed. This is only delivered on a {@link SubscriptionsListenRequestsubscriptions/listen} stream when the client requested it via the `toolsListChanged` filter field.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/tools/list_changed"]
    params: NotificationParams | None = None


@dataclass(kw_only=True)
class CancelledNotificationParams:
    """
    Parameters for a `notifications/cancelled` notification.
    """

    meta: NotificationMetaObject | None = None
    reason: str | None = None
    """
    An optional string describing the reason for the cancellation. This MAY be logged or presented to the user.
    """
    request_id: RequestId
    """
    The ID of the request to cancel.

    This MUST correspond to the ID of a request the client previously issued.
    """


@dataclass(kw_only=True)
class ClientNotification:
    """
    This notification is sent by the client to indicate that it is cancelling a request it previously issued.

    On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

    The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

    This notification indicates that the result will be unused, so any associated processing SHOULD cease.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/cancelled"]
    params: CancelledNotificationParams


@dataclass(kw_only=True)
class ClientResult:
    root: Result
    """
    Common result fields.
    """


@dataclass(kw_only=True)
class ContentBlock:
    root: TextContent | ImageContent | AudioContent | ResourceLink | EmbeddedResource


@dataclass(kw_only=True)
class ElicitRequest:
    """
    A request from the server to elicit additional information from the user via the client.
    """

    method: Literal["elicitation/create"]
    params: ElicitRequestParams


@dataclass(kw_only=True)
class EmptyResult:
    root: Result
    """
    Common result fields.
    """


@dataclass(kw_only=True)
class JSONRPCResultResponse:
    """
    A successful (non-error) response to a request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: Result


@dataclass(kw_only=True)
class ListPromptsResult:
    """
    The result returned by the server for a {@link ListPromptsRequestprompts/list} request.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    next_cursor: str | None = None
    """
    An opaque token representing the pagination position after the last returned result.
    If present, there may be more results available.
    """
    prompts: list[Prompt]
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class ListPromptsResultResponse:
    """
    A successful response from the server for a {@link ListPromptsRequestprompts/list} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: ListPromptsResult


@dataclass(kw_only=True)
class ListResourceTemplatesResult:
    """
    The result returned by the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    next_cursor: str | None = None
    """
    An opaque token representing the pagination position after the last returned result.
    If present, there may be more results available.
    """
    resource_templates: list[ResourceTemplate]
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class ListResourceTemplatesResultResponse:
    """
    A successful response from the server for a {@link ListResourceTemplatesRequestresources/templates/list} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: ListResourceTemplatesResult


@dataclass(kw_only=True)
class ListResourcesResult:
    """
    The result returned by the server for a {@link ListResourcesRequestresources/list} request.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    next_cursor: str | None = None
    """
    An opaque token representing the pagination position after the last returned result.
    If present, there may be more results available.
    """
    resources: list[Resource]
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class ListResourcesResultResponse:
    """
    A successful response from the server for a {@link ListResourcesRequestresources/list} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: ListResourcesResult


@dataclass(kw_only=True)
class ListToolsResult:
    """
    The result returned by the server for a {@link ListToolsRequesttools/list} request.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    next_cursor: str | None = None
    """
    An opaque token representing the pagination position after the last returned result.
    If present, there may be more results available.
    """
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    tools: list[Tool]
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class ListToolsResultResponse:
    """
    A successful response from the server for a {@link ListToolsRequesttools/list} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: ListToolsResult


@dataclass(kw_only=True)
class LoggingMessageNotificationParams:
    """
    Parameters for a `notifications/message` notification.
    """

    meta: NotificationMetaObject | None = None
    data: Any
    """
    The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here.
    """
    level: LoggingLevel
    """
    The severity of this log message.
    """
    logger: str | None = None
    """
    An optional name of the logger issuing this message.
    """


@dataclass(kw_only=True)
class ProgressNotification:
    """
    An out-of-band notification used to inform the receiver of a progress update for a long-running request.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/progress"]
    params: ProgressNotificationParams


@dataclass(kw_only=True)
class PromptMessage:
    """
    Describes a message returned as part of a prompt.

    This is similar to {@link SamplingMessage}, but also supports the embedding of
    resources from the MCP server.
    """

    content: ContentBlock
    role: Role


@dataclass(kw_only=True)
class ResourceUpdatedNotification:
    """
    A notification from the server to the client, informing it that a resource has changed and may need to be read again. This is only sent for resources the client opted in to via the `resourceSubscriptions` field of a {@link SubscriptionsListenRequestsubscriptions/listen} request.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/resources/updated"]
    params: ResourceUpdatedNotificationParams


@dataclass(kw_only=True)
class SubscriptionsAcknowledgedNotification:
    """
    Sent by the server to acknowledge that a
    {@link SubscriptionsListenRequestsubscriptions/listen} subscription has been
    established and to report which notification types it agreed to honor.

    This notification MUST be the first message the server sends carrying the
    subscription's ID in `io.modelcontextprotocol/subscriptionId`. The server MUST
    NOT send any notification on the subscription before acknowledging it. On
    stdio, where every subscription shares one channel, this ordering is defined
    per subscription ID and not per channel: messages belonging to other
    subscriptions MAY be interleaved before it.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/subscriptions/acknowledged"]
    params: SubscriptionsAcknowledgedNotificationParams


@dataclass(kw_only=True)
class ToolResultContent:
    """
    The result of a tool use, provided by the user back to the assistant.
    """

    meta: MetaObject | None = None
    """
    Optional metadata about the tool result. Clients SHOULD preserve this field when
    including tool results in subsequent sampling requests to enable caching optimizations.
    """
    content: list[ContentBlock]
    """
    The unstructured result content of the tool use.

    This has the same format as {@link CallToolResult.content} and can include text, images,
    audio, resource links, and embedded resources.
    """
    is_error: bool | None = None
    """
    Whether the tool use resulted in an error.

    If true, the content typically describes the error that occurred.
    Default: false
    """
    structured_content: Any | None = None
    """
    An optional structured result value.

    This can be any JSON value (object, array, string, number, boolean, or null).
    If the tool defined an {@link Tool.outputSchema}, this SHOULD conform to that schema.
    """
    tool_use_id: str
    """
    The ID of the tool use this result corresponds to.

    This MUST match the ID from a previous {@link ToolUseContent}.
    """
    type: Literal["tool_result"]


@dataclass(kw_only=True)
class CallToolResult:
    """
    The result returned by the server for a {@link CallToolRequesttools/call} request.
    """

    meta: ResultMetaObject | None = None
    content: list[ContentBlock]
    """
    A list of content objects that represent the unstructured result of the tool call.
    """
    is_error: bool | None = None
    """
    Whether the tool call ended in an error.

    If not set, this is assumed to be false (the call was successful).

    Any errors that originate from the tool SHOULD be reported inside the result
    object, with `isError` set to true, _not_ as an MCP protocol-level error
    response. Otherwise, the LLM would not be able to see that an error occurred
    and self-correct.

    However, any errors in _finding_ the tool, an error indicating that the
    server does not support tool calls, or any other exceptional conditions,
    should be reported as an MCP error response.
    """
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    structured_content: Any | None = None
    """
    An optional JSON value that represents the structured result of the tool call.

    This can be any JSON value (object, array, string, number, boolean, or null)
    that conforms to the tool's outputSchema if one is defined.
    """


@dataclass(kw_only=True)
class CancelledNotification:
    """
    This notification is sent by the client to indicate that it is cancelling a request it previously issued.

    On stdio, the server also sends this notification, solely to terminate a {@link SubscriptionsListenRequestsubscriptions/listen} stream: it references the ID of the `subscriptions/listen` request that opened the stream. Servers MUST NOT use this notification to cancel any other request.

    The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

    This notification indicates that the result will be unused, so any associated processing SHOULD cease.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/cancelled"]
    params: CancelledNotificationParams


@dataclass(kw_only=True)
class GetPromptResult:
    """
    The result returned by the server for a {@link GetPromptRequestprompts/get} request.
    """

    meta: ResultMetaObject | None = None
    description: str | None = None
    """
    An optional description for the prompt.
    """
    messages: list[PromptMessage]
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """


@dataclass(kw_only=True)
class JSONRPCMessage:
    root: JSONRPCRequest | JSONRPCNotification | JSONRPCResultResponse | JSONRPCErrorResponse
    """
    Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.
    """


@dataclass(kw_only=True)
class JSONRPCResponse:
    root: JSONRPCResultResponse | JSONRPCErrorResponse
    """
    A response to a request, containing either the result or error.
    """


@dataclass(kw_only=True)
class LoggingMessageNotification:
    """
    JSONRPCNotification of a log message passed from server to client. The client opts in by setting `"io.modelcontextprotocol/logLevel"` in a request's `_meta`.
    """

    jsonrpc: Literal["2.0"]
    method: Literal["notifications/message"]
    params: LoggingMessageNotificationParams


@dataclass(kw_only=True)
class SamplingMessageContentBlock:
    root: TextContent | ImageContent | AudioContent | ToolUseContent | ToolResultContent


@dataclass(kw_only=True)
class ServerNotification:
    root: (
        CancelledNotification
        | ProgressNotification
        | ResourceListChangedNotification
        | SubscriptionsAcknowledgedNotification
        | ResourceUpdatedNotification
        | PromptListChangedNotification
        | ToolListChangedNotification
        | LoggingMessageNotification
    )


@dataclass(kw_only=True)
class CreateMessageResult:
    """
    The result returned by the client for a {@link CreateMessageRequestsampling/createMessage} request.
    The client should inform the user before returning the sampled message, to allow them
    to inspect the response (human in the loop) and decide whether to allow the server to see it.
    """

    meta: MetaObject | None = None
    content: (
        TextContent
        | ImageContent
        | AudioContent
        | ToolUseContent
        | ToolResultContent
        | list[SamplingMessageContentBlock]
    )
    model: str
    """
    The name of the model that generated the message.
    """
    role: Role
    stop_reason: str | None = None
    """
    The reason why sampling stopped, if known.

    Standard values:
    - `"endTurn"`: Natural end of the assistant's turn
    - `"stopSequence"`: A stop sequence was encountered
    - `"maxTokens"`: Maximum token limit was reached
    - `"toolUse"`: The model wants to use one or more tools

    This field is an open string to allow for provider-specific stop reasons.
    """


@dataclass(kw_only=True)
class InputResponse:
    root: CreateMessageResult | ListRootsResult | ElicitResult


@dataclass(kw_only=True)
class InputResponses:
    """
    A map of client responses to server-initiated requests.
    Keys correspond to the keys in the {@link InputRequests} map;
    values are the client's result for each request.
    """

    root: dict[str, InputResponse]


@dataclass(kw_only=True)
class SamplingMessage:
    """
    Describes a message issued to or received from an LLM API.
    """

    meta: MetaObject | None = None
    content: (
        TextContent
        | ImageContent
        | AudioContent
        | ToolUseContent
        | ToolResultContent
        | list[SamplingMessageContentBlock]
    )
    role: Role


@dataclass(kw_only=True)
class CallToolRequest:
    """
    Used by the client to invoke a tool provided by the server.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["tools/call"]
    params: CallToolRequestParams


@dataclass(kw_only=True)
class CallToolRequestParams:
    """
    Parameters for a `tools/call` request.
    """

    meta: RequestMetaObject
    arguments: dict[str, Any] | None = None
    """
    Arguments to use for the tool call.
    """
    input_responses: InputResponses | None = None
    name: str
    """
    The name of the tool.
    """
    request_state: str | None = None


@dataclass(kw_only=True)
class CallToolResultResponse:
    """
    A successful response from the server for a {@link CallToolRequesttools/call} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: InputRequiredResult | CallToolResult


@dataclass(kw_only=True)
class Elicitation:
    """
    Present if the client supports elicitation from the server.
    """

    form: JSONObject | None = None
    url: JSONObject | None = None


@dataclass(kw_only=True)
class Sampling:
    """
    Present if the client supports sampling from an LLM.
    """

    context: JSONObject | None = None
    """
    Whether the client supports context inclusion via `includeContext` parameter.
    If not declared, servers SHOULD only use `includeContext: "none"` (or omit it).
    """
    tools: JSONObject | None = None
    """
    Whether the client supports tool use via `tools` and `toolChoice` parameters.
    """


@dataclass(kw_only=True)
class ClientCapabilities:
    """
    Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.
    """

    elicitation: Elicitation | None = None
    """
    Present if the client supports elicitation from the server.
    """
    experimental: dict[str, JSONObject] | None = None
    """
    Experimental, non-standard capabilities that the client supports.
    """
    extensions: dict[str, JSONObject] | None = None
    """
    Optional MCP extensions that the client supports. Keys are extension identifiers
    (e.g., "io.modelcontextprotocol/oauth-client-credentials"), and values are
    per-extension settings objects. An empty object indicates support with no settings.

    Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
    mandatory prefix.
    """
    roots: dict[str, Any] | None = None
    """
    Present if the client supports listing roots.
    """
    sampling: Sampling | None = None
    """
    Present if the client supports sampling from an LLM.
    """


@dataclass(kw_only=True)
class CompleteRequest:
    """
    A request from the client to the server, to ask for completion options.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["completion/complete"]
    params: CompleteRequestParams


@dataclass(kw_only=True)
class CompleteRequestParams:
    """
    Parameters for a `completion/complete` request.
    """

    meta: RequestMetaObject
    argument: Argument
    """
    The argument's information
    """
    context: Context | None = None
    """
    Additional, optional context for completions
    """
    ref: PromptReference | ResourceTemplateReference


@dataclass(kw_only=True)
class CreateMessageRequest:
    """
    A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.
    """

    method: Literal["sampling/createMessage"]
    params: CreateMessageRequestParams


@dataclass(kw_only=True)
class CreateMessageRequestParams:
    """
    Parameters for a `sampling/createMessage` request.
    """

    include_context: Literal["allServers", "none", "thisServer"] | None = None
    """
    A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.
    The client MAY ignore this request.

    Default is `"none"`. The values `"thisServer"` and `"allServers"` are deprecated (SEP-2596): servers SHOULD
    omit this field or use `"none"`, and SHOULD only use the deprecated values if the client declares
    {@link ClientCapabilities.sampling.context}.
    """
    max_tokens: int
    """
    The requested maximum number of tokens to sample (to prevent runaway completions).

    The client MAY choose to sample fewer tokens than the requested maximum.
    """
    messages: list[SamplingMessage]
    metadata: JSONObject | None = None
    """
    Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific.
    """
    model_preferences: ModelPreferences | None = None
    """
    The server's preferences for which model to select. The client MAY ignore these preferences.
    """
    stop_sequences: list[str] | None = None
    system_prompt: str | None = None
    """
    An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt.
    """
    temperature: float | None = None
    tool_choice: ToolChoice | None = None
    """
    Controls how the model uses tools.
    The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared.
    Default is `{ mode: "auto" }`.
    """
    tools: list[Tool] | None = None
    """
    Tools that the model may use during generation.
    The client MUST return an error if this field is provided but {@link ClientCapabilities.sampling.tools} is not declared.
    """


@dataclass(kw_only=True)
class DiscoverRequest:
    """
    A request from the client asking the server to advertise its supported
    protocol versions, capabilities, and other metadata. Servers **MUST**
    implement `server/discover`. Clients **MAY** call it but are not required
    to — version negotiation can also happen inline via per-request `_meta`.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["server/discover"]
    params: RequestParams


@dataclass(kw_only=True)
class DiscoverResult:
    """
    The result returned by the server for a {@link DiscoverRequestserver/discover} request.
    """

    meta: ResultMetaObject | None = None
    cache_scope: Literal["private", "public"]
    """
    Indicates the intended scope of the cached response, analogous to HTTP
    `Cache-Control: public` vs `Cache-Control: private`.

    - `"public"`: The response does not contain user-specific data. Any
      client or intermediary (e.g., shared gateway, caching proxy) MAY cache
      the response and serve it across authorization contexts.
    - `"private"`: The response MAY be cached and reused only within the
      same authorization context. Caches MUST NOT be shared across
      authorization contexts (e.g., a different access token requires a
      different cache).
    """
    capabilities: ServerCapabilities
    """
    The capabilities of the server.
    """
    instructions: str | None = None
    """
    Natural-language guidance describing the server and its features.

    This can be used by clients to improve an LLM's understanding of
    available tools (e.g., by including it in a system prompt). It should
    focus on information that helps the model use the server effectively
    and should not duplicate information already in tool descriptions.
    """
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """
    supported_versions: list[str]
    """
    MCP Protocol Versions this server supports. The client should choose a
    version from this list for use in subsequent requests.
    """
    ttl_ms: int
    """
    A hint from the server indicating how long (in milliseconds) the
    client MAY cache this response before re-fetching. Semantics are
    analogous to HTTP Cache-Control max-age.

    - If 0, The response SHOULD be considered immediately stale,
      The client MAY re-fetch every time the result is needed.
    - If positive, the client SHOULD consider the result fresh for this many
      milliseconds after receiving the response.
    """


@dataclass(kw_only=True)
class DiscoverResultResponse:
    """
    A successful response from the server for a {@link DiscoverRequestserver/discover} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: DiscoverResult


@dataclass(kw_only=True)
class GetPromptRequest:
    """
    Used by the client to get a prompt provided by the server.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["prompts/get"]
    params: GetPromptRequestParams


@dataclass(kw_only=True)
class GetPromptRequestParams:
    """
    Parameters for a `prompts/get` request.
    """

    meta: RequestMetaObject
    arguments: dict[str, str] | None = None
    """
    Arguments to use for templating the prompt.
    """
    input_responses: InputResponses | None = None
    name: str
    """
    The name of the prompt or prompt template.
    """
    request_state: str | None = None


@dataclass(kw_only=True)
class GetPromptResultResponse:
    """
    A successful response from the server for a {@link GetPromptRequestprompts/get} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: InputRequiredResult | GetPromptResult


@dataclass(kw_only=True)
class InputRequiredResult:
    """
    An InputRequiredResult sent by the server to indicate that additional input is needed
    before the request can be completed.

    At least one of `inputRequests` or `requestState` MUST be present.
    """

    meta: ResultMetaObject | None = None
    input_requests: InputRequests | None = None
    request_state: str | None = None
    result_type: str
    """
    Indicates the type of the result, which allows the client to determine
    how to parse the result object.

    Servers implementing this protocol version MUST include this field.
    For backward compatibility, when a client receives a result from a
    server implementing an earlier protocol version (which does not include
    `resultType`), the client MUST treat the absent field as `"complete"`.
    """


@dataclass(kw_only=True)
class InputResponseRequestParams:
    meta: RequestMetaObject
    input_responses: InputResponses | None = None
    request_state: str | None = None


@dataclass(kw_only=True)
class ListPromptsRequest:
    """
    Sent from the client to request a list of prompts and prompt templates the server has.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["prompts/list"]
    params: PaginatedRequestParams


@dataclass(kw_only=True)
class ListResourceTemplatesRequest:
    """
    Sent from the client to request a list of resource templates the server has.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["resources/templates/list"]
    params: PaginatedRequestParams


@dataclass(kw_only=True)
class ListResourcesRequest:
    """
    Sent from the client to request a list of resources the server has.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["resources/list"]
    params: PaginatedRequestParams


@dataclass(kw_only=True)
class ListToolsRequest:
    """
    Sent from the client to request a list of tools the server has.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["tools/list"]
    params: PaginatedRequestParams


@dataclass(kw_only=True)
class Data:
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """

    required_capabilities: ClientCapabilities
    """
    The capabilities the server requires from the client to process this request.
    """


@dataclass(kw_only=True)
class Error2(Error):
    code: Literal[-32021]
    """
    The error type that occurred.
    """
    data: Data
    """
    Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).
    """


@dataclass(kw_only=True)
class MissingRequiredClientCapabilityError:
    """
    Returned when processing a request requires a capability the client did not
    declare in `clientCapabilities`. For HTTP, the response status code MUST be
    `400 Bad Request`.
    """

    error: Error2
    id: RequestId | None = None
    jsonrpc: Literal["2.0"]


@dataclass(kw_only=True)
class PaginatedRequest:
    id: RequestId
    jsonrpc: Literal["2.0"]
    method: str
    params: PaginatedRequestParams


@dataclass(kw_only=True)
class PaginatedRequestParams:
    """
    Common params for paginated requests.
    """

    meta: RequestMetaObject
    cursor: str | None = None
    """
    An opaque token representing the current pagination position.
    If provided, the server should return results starting after this cursor.
    """


@dataclass(kw_only=True)
class ReadResourceRequest:
    """
    Sent from the client to the server, to read a specific resource URI.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["resources/read"]
    params: ReadResourceRequestParams


@dataclass(kw_only=True)
class ReadResourceRequestParams:
    """
    Parameters for a `resources/read` request.
    """

    meta: RequestMetaObject
    input_responses: InputResponses | None = None
    request_state: str | None = None
    uri: str
    """
    The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.
    """


@dataclass(kw_only=True)
class ReadResourceResultResponse:
    """
    A successful response from the server for a {@link ReadResourceRequestresources/read} request.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    result: InputRequiredResult | ReadResourceResult


@dataclass(kw_only=True)
class RequestMetaObject:
    """
    Extends {@link MetaObject} with additional request-specific fields. All key naming rules from `MetaObject` apply.
    """

    io_modelcontextprotocol_client_capabilities: ClientCapabilities
    """
    The client's capabilities for this specific request. Required.

    Capabilities are declared per-request rather than once at initialization;
    an empty object means the client supports no optional capabilities.
    Servers MUST NOT infer capabilities from prior requests.
    """
    io_modelcontextprotocol_client_info: Implementation | None = None
    """
    Identifies the client software making the request. Clients SHOULD
    include this field on every request unless specifically configured not
    to do so.

    The {@link Implementation} schema requires `name` and `version`; other
    fields are optional.

    The value is self-reported by the client and is not verified by the
    protocol. It is intended for display, logging, and debugging. Servers
    SHOULD NOT use it to change their behavior, and SHOULD NOT rely on it for
    security decisions.
    """
    io_modelcontextprotocol_log_level: LoggingLevel | None = None
    """
    The desired log level for this request. Optional.

    If absent, the server MUST NOT send any {@link LoggingMessageNotificationnotifications/message}
    notifications for this request. The client opts in to log messages by
    explicitly setting a level. Replaces the former `logging/setLevel` RPC.
    """
    io_modelcontextprotocol_protocol_version: str
    """
    The MCP Protocol Version being used for this request. Required.

    For the HTTP transport, this value MUST match the `MCP-Protocol-Version`
    header; otherwise the server MUST return a `400 Bad Request`. If the
    server does not support the requested version, it MUST return an
    {@link UnsupportedProtocolVersionError}.
    """
    progress_token: ProgressToken | None = None
    """
    If specified, the caller is requesting out-of-band progress notifications for this request (as represented by {@link ProgressNotificationnotifications/progress}). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.
    """


@dataclass(kw_only=True)
class RequestParams:
    """
    Common params for any request.
    """

    meta: RequestMetaObject


@dataclass(kw_only=True)
class ResourceRequestParams:
    """
    Common params for resource-related requests.
    """

    meta: RequestMetaObject
    uri: str
    """
    The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.
    """


@dataclass(kw_only=True)
class ServerCapabilities:
    """
    Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.
    """

    completions: JSONObject | None = None
    """
    Present if the server supports argument autocompletion suggestions.
    """
    experimental: dict[str, JSONObject] | None = None
    """
    Experimental, non-standard capabilities that the server supports.
    """
    extensions: dict[str, JSONObject] | None = None
    """
    Optional MCP extensions that the server supports. Keys are extension identifiers
    (e.g., "io.modelcontextprotocol/tasks"), and values are per-extension settings
    objects. An empty object indicates support with no settings.

    Keys MUST follow the {@link MetaObject`_meta` key naming rules}, with a
    mandatory prefix.
    """
    logging: JSONObject | None = None
    """
    Present if the server supports sending log messages to the client.
    """
    prompts: Prompts | None = None
    """
    Present if the server offers any prompt templates.
    """
    resources: Resources | None = None
    """
    Present if the server offers any resources to read.
    """
    tools: Tools | None = None
    """
    Present if the server offers any tools to call.
    """


@dataclass(kw_only=True)
class SubscriptionsListenRequest:
    """
    Sent from the client to open a long-lived channel for receiving notifications
    outside the context of a specific request. Replaces the previous HTTP GET
    endpoint and ensures consistent behavior between HTTP and STDIO.
    """

    id: RequestId
    jsonrpc: Literal["2.0"]
    method: Literal["subscriptions/listen"]
    params: SubscriptionsListenRequestParams


@dataclass(kw_only=True)
class SubscriptionsListenRequestParams:
    """
    Parameters for a {@link SubscriptionsListenRequestsubscriptions/listen} request.
    """

    meta: RequestMetaObject
    notifications: SubscriptionFilter
    """
    The notifications the client opts in to on this stream. The server
    **MUST NOT** send notification types the client has not explicitly
    requested.
    """


@dataclass(kw_only=True)
class InputRequest:
    root: CreateMessageRequest | ListRootsRequest | ElicitRequest


@dataclass(kw_only=True)
class ServerResult:
    root: (
        Result
        | InputRequiredResult
        | DiscoverResult
        | ListResourcesResult
        | ListResourceTemplatesResult
        | ReadResourceResult
        | SubscriptionsListenResult
        | ListPromptsResult
        | GetPromptResult
        | ListToolsResult
        | CallToolResult
        | CompleteResult
    )


@dataclass(kw_only=True)
class ClientRequest:
    root: (
        DiscoverRequest
        | ListResourcesRequest
        | ListResourceTemplatesRequest
        | ReadResourceRequest
        | SubscriptionsListenRequest
        | ListPromptsRequest
        | GetPromptRequest
        | ListToolsRequest
        | CallToolRequest
        | CompleteRequest
    )


@dataclass(kw_only=True)
class InputRequests:
    """
    A map of server-initiated requests that the client must fulfill.
    Keys are server-assigned identifiers; values are the request objects.
    """

    root: dict[str, InputRequest]


@dataclass(kw_only=True)
class JSONArray:
    root: list["JSONValue"]


@dataclass(kw_only=True)
class JSONObject:
    root: dict[str, "JSONValue"]


@dataclass(kw_only=True)
class JSONValue:
    root: Union[JSONObject, list["JSONValue"], str | int | float | bool | None]


AnyCallToolResult = CallToolResult | InputRequiredResult
AnyGetPromptResult = GetPromptResult | InputRequiredResult
AnyReadResourceResult = ReadResourceResult | InputRequiredResult
