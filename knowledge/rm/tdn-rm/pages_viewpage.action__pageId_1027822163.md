---
content_hash: 25c988604d167ced90a257df858698382f463cb7d7e74dc2050aaa0b294d002b
fetched_at: '2026-06-29T00:05:48.708513+00:00'
page_id: '1027822163'
product: rm
source: tdn-rm
title: Informações relativas ao Destinatário (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1027822163
version: 6
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | pai | Obrigatório | Origem | Descrição |
| **destinatario** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **Não** | **Grupo** | **Grupo de informações relativas ao Destinatário** |
| cnpjcpf | destinatario | Não | aba **“Dest. Serviço”**Campo **→** TMOVFISCAL/CNPJCPFDESTSERV | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) ou Cadastro Nacional de Pessoa Física (CPF) do destinatário de serviço |
| nif | destinatario | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NIFDESTSERV | Número de identificação fiscal fornecido por órgão de administração tributária no exterior |
| codNaoNIF | destinatario | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NAONIFDESTSERV | Motivo para não informação do NIF:    0 - Não informado na nota de origem;  1 - Dispensado do NIF;  2 - Não exigência do NIF; |
| nome | destinatario | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NOMEDESTSERV | Nome / Nome Empresarial do destinatário |
| **endereco** | **destinatario** | Não |  | Grupo de informações do endereço do destinatário do serviço. |
| logradouro | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/RUADESTSERV | Tipo e nome do logradouro do endereço do destinatário do serviço. |
| numero | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NUMERODESTSERV | Número no logradouro do endereço do destinatário do serviço. |
| complemento | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/COMPLDESTSERV | Complemento do endereço do destinatário do serviço. |
| bairro | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/BAIRRODESTSERV | Bairro do endereço do destinatário do serviço. |
| codigoMunicipio | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODMUNICIPIODESTSERV | Código do município do endereço do destinatário do serviço.   (Tabela do IBGE) |
| nomeMunicipio | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODMUNICIPIODESTSERV  Retorna o nome do município | Nome da cidade no exterior do destinatário do serviço. |
| cep | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CEPDESTSERV | Grupo de informações do endereço no exterior. |
| pais | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODPAISDESTSERV | Código do país do endereço do destinatário do serviço.   (Tabela de Países ISO) |
| estadoProvinciaExterior | endereco | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODETDDESTSERV  Retorna o nome do estado | Estado, província ou região da cidade no exterior do destinatário do serviço. |
| **contato** | **destinatario** | Sim |  | Representação completa do contato do Destinatário |
| fone | contato | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/TELEFONEDESTSERV | Número do telefone do destinatário.  (Preencher com o Código DDD + número do telefone.  Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) |
| email | contato | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/EMAILDESTSERV | E-mail do destinatário. |
