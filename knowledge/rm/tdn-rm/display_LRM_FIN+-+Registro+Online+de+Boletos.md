---
content_hash: 8b3ce456faa7c6c80a4f5df8914ad390781551777d0ad0c33d22752c3a11bf0c
fetched_at: '2026-06-29T00:09:18.084040+00:00'
page_id: '421388660'
product: rm
source: tdn-rm
title: FIN - Registro Online de Boletos
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Registro+Online+de+Boletos
version: 73
---

Na inclusão de boleto, ao selecionar a opção 'Registrar Online o Boleto' na etapa Dados do Boleto, o sistema comunica com o serviço do banco para registro, enviando as informações do boleto para o banco e alterando o status de remessa do boleto para 'Registrado Online'. Este boleto será criado com o código de barras e IPTE, pois o processo de remessa é executado na inclusão.

Para que o registro online possa ser executado com sucesso, o convênio deve estar parametrizado corretamente, na aba 'Registro Online' selecionando a opção 'Permite registro de boleto online', informando os dados do sistema de cobrança e URL de registro do banco.  
Caso alguma informação esteja incorreta para o processo de registro online, irá ser exibido o log de divergência informando o ponto a ser ajustado, que é retornado pelo serviço de registro do banco. Também é possível visualizar o XML/JSON enviado para o banco com as informações do boleto. Neste caso o boleto será incluído normalmente podendo ser realizado o registro online após a correção da divergência informada no log do processo.

Após o registro do boleto, caso seja necessário, é possível cancelar o registro de forma online. O processo de cancelamento online do registro está disponível apenas para alguns bancos. Saiba mais em **.**

**Observações**:

Na inclusão de boleto para mais de um lançamento, caso algum dos lançamentos apresentem divergência no registro, o sistema inclui os boletos para os lançamentos exibindo log detalhado ao fim do processo.  
O XML/JSON enviado para o banco, estará disponível na visão do boleto na aba *Dados CNAB*em *'*Registro de Boleto Online', podendo ser visualizado em TXT após a execução do processo. Obs: O arquivo XML/JSON é exibido somente quando ocorrer alguma divergência, no log ao fim do processo de registro online do boleto.

Quando selecionado mais de um lançamento, não é realizada a verificação dos convênios configurados para registro online, para que não haja perda de desempenho do sistema na inclusão, mesmo que nenhum dos lançamentos selecionados estejam vinculados a convênios parametrizados para trabalhar com registro online, a flag 'Registrar Online o Boleto' é habilitada. Esta verificação é realizada pelo serviço de registro online.

**Bancos homologados**

As informações abaixo serão atualizadas conforme a disponibilização dos bancos:

| Banco | Modelo (s) de registro | Permite alteração | Permite cancelamento |
| --- | --- | --- | --- |
| [Santander](https://tdn.totvs.com/display/LRM/Registro+online+Santander) | v1 e v2 | SIM (v2) | SIM (v2) |
| [Bradesco](https://tdn.totvs.com/display/LRM/Registro+online+Bradesco) | v1 e v2 | NÃO | SIM (v2) |
| [Itaú](https://tdn.totvs.com/pages/viewpage.action?pageId=923177961) | v1 e v2 | SIM (v2) | SIM (v2) |
| [Banco do Brasil](https://tdn.totvs.com/display/LRM/Registro+online+Banco+do+Brasil) | v1 e v2 | SIM (v2) | SIM (v2) |
| [Caixa Econômica Federal](https://tdn.totvs.com/pages/viewpage.action?pageId=934631303) | v1 | NÃO | NÃO |
| [Sicredi](https://tdn.totvs.com/display/LRM/Registro+online+Sicredi) | v1 e v2 | NÃO | SIM (v2) |
| [Banrisul](https://tdn.totvs.com/display/LRM/Registro+online+Banrisul) | v1 | NÃO | NÃO |
| [Sicoob](https://tdn.totvs.com/pages/viewpage.action?pageId=552577668) | v1, v2 e v3 | SIM (v2) | SIM (v2 e v3) |
| [Grafeno](https://tdn.totvs.com/display/LRM/Registro+online+Grafeno) | v1 | NÃO | NÃO |
| [Banestes](https://tdn.totvs.com/display/LRM/Registro+online+Banestes) | v1 | NÃO | NÃO |
| [AutBank (Crefisa/b.Uni/Daycoval)](https://tdn.totvs.com/pages/viewpage.action?pageId=976136223). | v1 | SIM | SIM |

**Boletos incluídos sem Registro**

Para boletos criados e não registrados online, basta selecionar o boleto para ser executado pela visão de Lançamentos em Anexos | Processos | Registro online de Boletos ou pela visão de Boletos em Processos / Registro Online de Boletos.  
O Boleto também pode ser registrado online via Web Service através de XML, alterando o status de remessa do boleto para Registrado Online.

**Registro Online de Boletos por Filtro**

O processo foi criado para registrar online um grande volume de boletos de acordo com o filtro aplicado, sem necessidade de selecionar o boleto na visão. Esta funcionalidade encontra-se disponível no menu Movimentações Bancárias | Integração Bancária | Processos em Lote | .

**Inclusão via Web Service**

O boleto pode ser incluso registrado online via Web Service, utilizando a tag <RegistrarOnLineBoleto>true</RegistrarOnLineBoleto>. Esta irá selecionar a opção 'Registrar Online o Boleto' na execução do processo, incluindo o boleto com o status de remessa Registrado Online.

**Certificado Digital**

É necessário entrar em contato com o banco para se informar sobre a necessidade da utilização do certificado.  
Obs.: Para cadastrar o certificado digital no TOTVS Gestão Financeira e necessário importar o arquivo .pfx ou .p12 no menu Cadastros | Fiscais | Mais... | Certificado Digital. A TOTVS não disponibiliza certificados de nenhum dos bancos, por ser tratar de identificação individual para cada empresa.

**Truncamento de campos do cadastro do Cliente/Fornecedor ao Registrar Boleto online**

Ao executar o processo de registro online de boleto, caso a quantidade de caracteres dos campos do endereço e nome do cadastro do Cli/For, seja maior que a quantidade de caracteres informada no layout de cada banco, o sistema irá truncar esses campos de acordo com cada manual.

**Motivo de recusa do Registro Online**

No caso de recusa de registro online do boleto pelo banco o motivo dessa recusa será gravado no campo MOTIVORECUSAREGISTROONLINE da FBOLETO e a mensagem retornada pelo banco com o motivo da recusa será gravada no boleto no campo '[Motivo de recusa do Registro Online](https://tdn.totvs.com/display/LRM/DT+Motivo+da+Recusa+do+Registro+Online+de+Boleto)'. Esse campo será atualizado quando o registro online for recusado, nele só será armazenado o último registro e quando registro online for aceito o campo será limpo.

**Atualização do CNABSTATUS (Status da Remessa) do boleto quando recusado pelo banco no Registro Online**

Quando o boleto for recusado pelo banco no processo de registro online o status da remessa do boleto será atualizado para “Recusado”.

**Campos de layout do Registro Online**

Para que os dados do registro online sejam enviados para o banco deve ser cadastrado os campos do layout através da opção "[Layout Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online)" (localizado no cadastro do Banco, disponível no menu Movimentações Bancárias | Bancos e Agências) de acordo com o manual do Banco. **Exemplo**: Abaixo um exemplo de agrupamento e tags do campo do layout **beneficiario.conta\_beneficiario**, onde:

1. **beneficiario:** é o agrupador das informações do beneficiário que será enviada ao banco;
2. (**.**)**Ponto:** é o separador do Agrupador e da Tag;
3. **conta\_beneficiario:**é a tag que receberá a informação do beneficiário que é enviado para o banco.

A imagem mostra como no arquivo as informações serão enviadas para o banco:

Como informar no sistema:

  Recursos Adicionais

* [Cadastro de Certificado Digital](http://tdn.totvs.com/x/WoovGQ)
* [Associação do Layout do Registro Online](http://tdn.totvs.com/x/1_EdGQ)
* [Inclusão de Boleto Registrado Online](http://tdn.totvs.com/pages/viewpage.action?pageId=273997002)
* [Registro Online para boletos inclusos](http://tdn.totvs.com/display/public/LRM/DT+Registro+Online+de+Boletos)
* [Registro on-line de boletos por filtro](https://tdn.totvs.com/display/LRM/Registro+on-line+de+boletos+por+filtro)
* [Visualizar XML/JSON do Registro Online no boleto](http://tdn.totvs.com/pages/viewpage.action?pageId=286499982)
* [Motivo da Recusa do Registro Online de Boleto](http://tdn.totvs.com/x/meAfGg)
* [Alteração online da Data de Vencimento](https://tdn.totvs.com/pages/viewpage.action?pageId=784778381)
