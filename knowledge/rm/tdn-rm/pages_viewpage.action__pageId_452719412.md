---
content_hash: efdb94f352b02cd4c1bcb82bb5861a5ddd4cb2459f4aae87ad905a024530d6b5
fetched_at: '2026-06-29T00:10:07.362698+00:00'
page_id: '452719412'
product: rm
source: tdn-rm
title: S-1200 – Remuneração do Trabalhador vinculado ao RGPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719412
version: 3
---

São as informações da remuneração de cada trabalhador no mês de referência. Este evento deve ser utilizado para todos os trabalhadores filiados ao Regime Geral de Previdência Social – RGPS a serviço do empregador/contribuinte/órgão público, constantes na Tabela 1 – Categorias de Trabalhadores.

**Observações:**

* + Caso a coligada utilize tomador de Serviços, a estrutura desse evento será criada conforme a distribuição do Sefip, ou seja, as verbas serão discriminadas de acordo com o valor rateado por tomador que terá vínculo a uma Lotação Tributária.
  + Caso o funcionário seja elegível para o lançamento do evento com Código de Cálculo 315 - BASE DE FGTS DE AFASTADOS, e este evento não esteja na ficha financeira ou na distribuição do Sefip, o sistema acusará mensagem de erro informando que o funcionário esteve afastado e não possui o respectivo evento.
  + Para os funcionários que possuem movimento no período de apuração com todos os eventos gerados, o sistema gerará os eventos S-1200 e S-1210. Caso desejar que não sejam gerados esses eventos, será necessário cancelar a movimentação desse funcionário, pois quando não existe período criado, esses eventos não serão gerados.

**Autônomos Externos | Internos**

* Para considerar os autônomos externos neste evento, é necessário realizar a importação do registro do autônomo para o cadastro de Autônomos Externos.
* Para configurar as verbas de Provento e Desconto que serão utilizadas na integração dos autônomos provenientes de outros sistemas, o usuário deve acessar o Parametrizador, selecionar a opção **06.07 - eSocial** e prosseguir até a etapa dedicada aos **Autônomos Externos**.
* É necessário gerar o lançamento financeiro para o autônomo externo, com o objetivo de apurar os encargos financeiros antes de realizar a geração do evento S-1200.
* Após realizar os passos mencionados anteriormente, o usuário deve executar o processo de "Gerar XML" selecionando o evento S-1200 e marcando a flag "Gerar Autônomo Fluxus/Externos".
* Na integração do evento S-1200 com o TAF, será criado automaticamente um cadastro separado do Autônomo Externo de acordo com as informações presentes no grupo infoComplem.
* O evento S-1200 será gerado para autônomos do TOTVS Gestão Financeira, mesmo nos casos em que os documentos estão configurados apenas como "Gera IRRF", e não há retenção do imposto devido à base de cálculo insuficiente para o desconto. O campo "Tipo de Documento" pode ser configurado no TOTVS Gestão Financeira, acessando o menu BackOffice | Gestão Financeira | Cadastros | Clientes/Fornecedores | Anexos | Lançamentos.

**Considerações sobre algumas tag's geradas no arquivo**

* Grupo infoInterm e infoTrabInterm  
  Para a correta geração das informações, dentro do cadastro de intermitente se faz necessário a vinculação de um envelope de pagamento na competência na aba "Pagamentos" para as convocações.
* Tag qtdDiasInterm

Retorna a quantidade de dias presente na aba "Pagamentos".

* Tag codConv: Retorna o Código da Convocação.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Periódicos

Gerar XML  
[Como gerar as tags de remuneração outro emprego para autônomos do Totvs Gestão Financeira?](http://tdn.totvs.com/pages/editpage.action?pageId=421375083)

[Mapeamento das informações do evento](http://tdn.totvs.com/display/LRM/Evento+S-1200)
