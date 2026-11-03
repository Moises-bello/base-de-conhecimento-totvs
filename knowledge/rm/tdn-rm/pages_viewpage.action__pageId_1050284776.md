---
content_hash: 9f0cf5353984694a5664a994dc5666a49b1b5b78ea54ff4a094b4bbc6122131c
fetched_at: '2026-06-29T00:05:51.236175+00:00'
page_id: '1050284776'
product: rm
source: tdn-rm
title: Grupo de informações relativas ao Destinatário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050284776
version: 3
---

### [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| Dest | [impostoibscbs](https://tdn.totvs.com/pages/viewpage.action?pageId=1025223880) | Não | Grupo | Grupo de informações relativas ao Destinatário |
| cpfcnpj | Dest | Não | aba **“Dest. Serviço”**Campo **→** TMOVFISCAL/CNPJCPFDESTSERV | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) ou Cadastro Nacional de Pessoa Física (CPF) do destinatário de serviço |
| NIF | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NIFDESTSERV | Número de identificação fiscal fornecido por órgão de administração tributária no exterior |
| cNaoNIF | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NAONIFDESTSERV | Motivo para não informação do NIF:    0 - Não informado na nota de origem;  1 - Dispensado do NIF;  2 - Não exigência do NIF; |
| nome | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NOMEDESTSERV | Nome / Nome Empresarial do destinatário |
| logradouro | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/RUADESTSERV | Tipo e nome do logradouro do endereço do destinatário do serviço. |
| numend | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NUMERODESTSERV | Número no logradouro do endereço do destinatário do serviço. |
| complend | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/COMPLDESTSERV | Complemento do endereço do destinatário do serviço. |
| bairro | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/BAIRRODESTSERV | Bairro do endereço do destinatário do serviço. |
| cep | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CEPDESTSERV | Grupo de informações do endereço no exterior. |
| codmunibge | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODMUNICIPIODESTSERV | Código do município do endereço do destinatário do serviço.   (Tabela do IBGE) |
| cidade | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODMUNICIPIODESTSERV  Retorna o nome do município | Nome da cidade no exterior do destinatário do serviço. |
| estado | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODETDDESTSERV  Retorna o nome do estado | Estado, província ou região da cidade no exterior do destinatário do serviço. |
| codpais | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODPAISDESTSERV | Código do país do endereço do destinatário do serviço.   (Tabela de Países ISO) |
| ddd | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/TELEFONEDESTSERV | Número do telefone do destinatário.  (Preencher com o Código DDD + número do telefone.  Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) |
| telefone | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/TELEFONEDESTSERV | Número do telefone do destinatário.  (Preencher com o Código DDD + número do telefone.  Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) |
| email | Dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/EMAILDESTSERV | E-mail do destinatário. |
