---
content_hash: 8da60a096c6249da27d6cb3b8d6d0879069c1c89c7ba4792c1b7bb8957664d7f
fetched_at: '2026-06-29T00:05:47.765567+00:00'
page_id: '1017421770'
product: rm
source: tdn-rm
title: infDPS/IBSCBS/dest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1017421770
version: 6
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **dest** | **IBSCBS** | **Não** | **Grupo** | **Grupo de informações relativas ao Destinatário** |
| CNPJ | dest | Sim | aba **“Dest. Serviço”**Campo **→** TMOVFISCAL/CNPJCPFDESTSERV | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do destinatário de serviço |
| CPF | dest | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CNPJCPFDESTSERV | Número da inscrição no Cadastro Nacional de Pessoa Física (CPF) do destinatário do serviço |
| NIF | dest | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NIFDESTSERV | Número de identificação fiscal fornecido por órgão de administração tributária no exterior |
| cNaoNIF | dest | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NAONIFDESTSERV | Motivo para não informação do NIF:    0 - Não informado na nota de origem;  1 - Dispensado do NIF;  2 - Não exigência do NIF; |
| xNome | dest | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NOMEDESTSERV | Nome / Nome Empresarial do destinatário |
| **end** | **dest** | **Não** | **Grupo** | **Grupo de informações do endereço do destinatário do serviço.** |
| **endNac** | **end** | **Sim** | **Grupo** | **Grupo de informações do endereço nacional.** |
| cMun | endNac | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODMUNICIPIODESTSERV | Código do município do endereço do destinatário do serviço.   (Tabela do IBGE) |
| CEP | endNac | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CEPDESTSERV | Código numérico do Endereçamento Postal nacional (CEP)    do endereço do destinatário do serviço. |
| **endExt** | **end** | **Sim** | **Grupo** | **Grupo de informações do endereço no exterior.** |
| cPais | endExt | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODPAISDESTSERV | Código do país do endereço do destinatário do serviço.   (Tabela de Países ISO) |
| cEndPost | endExt | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODETDDESTSERV | Código alfanumérico do Endereçamento Postal no exterior do destinatário do serviço. |
| xCidade | endExt | Sim |  | Nome da cidade no exterior do destinatário do serviço. |
| xEstProvReg | endExt | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/CODETDDESTSERV | Estado, província ou região da cidade no exterior do destinatário do serviço. |
| xLgr | end | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/RUADESTSERV | Tipo e nome do logradouro do endereço do destinatário do serviço. |
| nro | end | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/NUMERODESTSERV | Número no logradouro do endereço do destinatário do serviço. |
| xCpl | end | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/COMPLDESTSERV | Complemento do endereço do destinatário do serviço. |
| xBairro | end | Sim | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/BAIRRODESTSERV | Bairro do endereço do destinatário do serviço. |
| fone | dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/TELEFONEDESTSERV | Número do telefone do destinatário.  (Preencher com o Código DDD + número do telefone.  Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) |
| email | dest | Não | aba **“Dest. Serviço”**Campo **→**  TMOVFISCAL/EMAILDESTSERV | E-mail do destinatário. |
