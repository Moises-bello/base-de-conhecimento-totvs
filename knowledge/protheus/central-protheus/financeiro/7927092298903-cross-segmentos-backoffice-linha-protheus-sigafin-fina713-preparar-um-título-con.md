---
article_id: 7927092298903
category: Financeiro
content_hash: 0c67adc043f084127661a15a950b7d51a2e1bdc8601ae527e4474d97a1e0229e
fetched_at: '2026-06-28T22:38:03.158402+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Preparar
  um título contas a receber para envio de Boleto Online - API Banco do Brasil (FINA713)
type: support-article
updated_at: '2026-01-20T20:12:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7927092298903-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Preparar-um-t%C3%ADtulo-contas-a-receber-para-envio-de-Boleto-Online-API-Banco-do-Brasil-FINA713
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19351815560087) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como preparar um título contas a receber para envio de Boleto Online - API Banco do Brasil (FINA713)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713 - Todas as versões  
  
**Solução**  
Para a geração do Boleto Online - API Banco do Brasil, precisamos configurar alguns cadastros.

**Cadastro de Cliente** (**MATA030**)   
Cadastrar um cliente baseado em um CNPJ fictício no site do banco do brasil  
Segue um print de tela do site do banco do brasil   
https://apoio.developers.bb.com.br/referency/post/5ffc477c3b02bd0012ecaa1a  
[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092005911)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092005911)  
**Nome da Empresa** | **CNPJ**  
TECIDOS FARIA DUARTE | 74910037000193  
LIVRARIA CUNHA DA CUNHA | 98959112000179  
DOCERIA BARBOSA DE ALMEIDA | 92862701000158  
DEPOSITO ALVES BRAGA | 94491202000127  
PAPELARIA FILARDES GARRIDO | 97257206000133

**Atualização de Banco** **(MATA070**)  
**Agência (A6\_AGÊNCIA)** sem digito  
**Conta( A6\_NUMCON)** sem digito  
**Banco Oficial (A6\_BCOOF )** = 001 (Banco do Brasil )  
**Campo Bloqueada (A6\_BLOCKED)** Precisa estar preenchido= 2

Atualiza **Parâmetro de Bancos** - CNAB (**FINA130**)  
  
**Aba Cadastrais**   
Cód. Empresa( **EE\_CODEMP** ) Convênio da empresa, disponibilizado pelo Banco do Brasil no link   
<https://apoio.developers.bb.com.br/referency/post/5ffc477c3b02bd0012ecaa1a>  
[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058831767)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058831767)  
**Cod. Empresa(EE\_CODEMP) =** 3128557 (número fictício para teste.)  
**Extensão**(**EE\_EXTEN**)= TXT  
**Faixa Inicio** (**EE\_FAXINI**) = 000000000001   
**Faixa Fim** (**EE\_FAXFIM**) = 999999999999  
**Faixa Atual** (**EE\_FAXATU** ) = 00000000001  
**Tabela** (**EE\_TABELA**) = 17  
**Nro Byte** (**EE\_NRBYTES**) = 240  
  
**Aba Outros**  
**Cód Carteira** (**EE\_CODCART**) = 17  
**Bco. Oficial** (**EE\_CODOFI**) = 001  ( Banco do Brasil )  
**Var. Carteira** (**EE\_VARCART**) = 035

* **Número Dias Limite Recebimento**deve ser informado no campo Dias Recebim**(EE\_DIASREC)**
  + Quando este campo possui um valor > 0, internamente o **Indicador Aceite Titulo Vencido** passa a ser enviado com 'S'
* **Quantidade Dias Protesto** deve ser informado no campo Dias Prot **(EE\_DIASPRT)**
* **Mensagem para instrução de cobrança**deve ser informada no campo Mensagem 1 **(EE\_FORMEN1)**, vale ressaltar que o banco aceita no máximo **165 caracteres.** Recomendamos o uso de letras minúsculas, pois na impressão do boleto existe um espaço pré-definido para exibição da mensagem.
* **Recebimento on-line**deverá ser informado para pelo menos um convênio quando o retorno(**FINA715 ou Webhook**) estiver configurado (**EE\_RETAUT**). Caso não esteja habilitado, o retorno não irá ser processado para esse convênio.

 - SIGACFG na opção "Schedule" faça a criação dos agendamento  
FINA713('01')  
Onde o ('01') seria o grupo da empresa  
E ao selecionar as filiais, marque somente 1 filial (Não selecione todas as filiais), pois o job já funciona por grupo de empresa.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092033943)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092033943)

**Importante:** Caso tiver mais de um ambiente com o job FINA713('01') configurado, ao executar poderá gerar falhar e não executar o job. Sugerimos que seja cadastrado o job FINA713('01')  em um único ambiente.

Poderá consultar se existe mais de um ambiente com o job configurado ao efetuar um select no campo XX1

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092045975)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092045975)

Acesse o FINA710 - Novo Painel Gestor e acesse "Comunicação Online" utilizando o menu  
E clique em "Configuração de Contas"  
  
[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058882455)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058882455)

Ao clicar em "Novo Layout"

Onde terá que selecionar o banco. E clique em "avançar"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092072727)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092072727)

Obtenha suas credencias acessando o site do banco

<https://app.developers.bb.com.br/>

Acesse "nova aplicação"  
E crie uma nova, selecionando a opção "Cobranças"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092097943)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092112023)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092112023)

E na opção do menu, acesse "Credenciais", onde terá acesso a suas chaves

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058946199)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058946199)

Volte no Protheus e marque  
Produção ou Homologação, pois o banco fornece credenciais diferente para cada ambiente.

Insira suas credenciais conforme o exemplo abaixo, e clique em "validar credenciais"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058953111)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058953111)

 - Configure o seu layout  
Opte em escolher os conteúdos dos campos que estiver usando nos seus cadastros

Exemplo:

Vou escolher a opção do conteúdo do campo A1\_CEP ao invés de A1\_CEPC, já que no meu ambiente o campo A1\_CEPC está vazio. Se eu escolhesse A1\_CEPC, no momento da transmissão poderá ocorrer falhar ou rejeição, por algum campo ir valor NULO.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058965271)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058965271)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092163863)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092163863)

Na rotina FINA060 - Colocar o titulo em Borderô, atentando-se aos campos  
**Banco**-> Banco do Brasil ( SA6 )  
**Situação**-> Não é possível com carteira 0  
**\*Sub Conta** -> Banco do Brasil  ( SEE )  
**\*Espécie** -> 2 Duplicata mercantil  
  
[![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7928641946903)](https://centraldeatendimento.totvs.com/hc/article_attachments/7928641946903)  
  
\*Para que os campos (**Sub Conta /Espécie** ) estejam disponibilizados, o campo **A6\_CFGAPI (SA6)** deve estar com conteúdo =**1 ou 3 para cadastro do Banco do Brasil.**

**Exemplo:**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7928728455447)

**Significado de cada status:**

**1=RECEBER REMESSA;**  
**2=SEM CONFIG.;**  
**3=RECEBER REMESSA E RETORNO**  
  
**Obs:** O campo **A6\_CFGAPI** ficará com o conteúdo 1 automaticamente quando o layout for configurado, ou 3 se for configurado o retorno também. [![](https://centraldeatendimento.totvs.com/hc/article_attachments/19351815570455)](https://centraldeatendimento.totvs.com/hc/article_attachments/19351815570455)

Ao concluir a inclusão do Borderô, já estará disponível no "**Monitor de boletos com Pendências**" na aba **À registrar** e com status de **À registrar**    
  
[![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7928744053911)](https://centraldeatendimento.totvs.com/hc/article_attachments/7928744053911)

SIGACFG > Schedule > Agendamento > Monitor  
Quando o job for executado, irá apresentar uma legenda verde que significa  
  
[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058987031)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530058987031)  
[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092184471)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530092184471)  
  
Após o termino da execução do job, a legenda deverá ser alterada para "cinza"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20530059012759)](https://centraldeatendimento.totvs.com/hc/article_attachments/20530059012759)

O registro irá sair da opção "A Registrar" o boleto esta disponível para Download.  
  
[![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7938565545239)](https://centraldeatendimento.totvs.com/hc/article_attachments/7938565545239)

**Possíveis erros para o Banco do Brasil**

 - Ao imprimir o boleto apresentar o erro:  
**412 - Sem acesso ao arquivo PDF**  
Erro  
Não foi possível acessar o arquivo \spool\boletos\01\00174910037000193083816.pdf.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20668829913751)](https://centraldeatendimento.totvs.com/hc/article_attachments/20668829913751)

Geralmente esse erro ocorre por falta do arquivo printer.exe dentro do /appserver/printer.exe

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20668851885975)](https://centraldeatendimento.totvs.com/hc/article_attachments/20668851885975)

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como atualizar o Totvs Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-atualizar-o-Totvs-Printer)

**- Detalhes do Erro - 500 InternalServerError**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20625209435031)](https://centraldeatendimento.totvs.com/hc/article_attachments/20625209435031)

Podemos observar que no console.log do appserver apresentou erro de credencial que deve ser verificado junto ao banco.

Neste exemplo eu forcei um erro, utilizei as minhas credenciais de base de homologação,  em um ambiente de produção, e por isso do erro abaixo.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20625209459735)](https://centraldeatendimento.totvs.com/hc/article_attachments/20625209459735)

grant\_type=client\_credentials&scope=cobrancas.boletos-info cobrancas.boletos-requisicao

HTTP/1.1 500 Internal Server Error

Access-Control-Allow-Credentials: false

x-br-com-bb-oat-servidor: pxl1oat00080\_oat-servidor-autorizacao-5

Response Body: Request failed.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20625239349271)](https://centraldeatendimento.totvs.com/hc/article_attachments/20625239349271)

**Saiba mais**  
Boleto Online  - FINA713 e Novo Gestor Financeiro (NGF ) - FINA710  
[Registro de boletos on-line - Banco do Brasil](https://tdn.totvs.com/display/public/PROT/Registro+de+boletos+on-line+-+Banco+do+Brasil)

[How to | - SIGAFIN - NGF - Como Config. Envio de Boletos FINA710](https://www.youtube.com/watch?v=OmxTYgputLo&t=42s)  
[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)  
[Comunicação bancária online - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=734394374)

API ITAU - [Registro de boletos on-line - Itaú](https://tdn.totvs.com/pages/releaseview.action?pageId=675571899)

API BRADESCO - [Registro de boletos on-line - Bradesco](https://tdn.totvs.com/display/PROT/Registro+de+boletos+on-line+-+Bradesco)
