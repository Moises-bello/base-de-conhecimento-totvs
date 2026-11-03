---
article_id: 20124950609815
category: Financeiro
content_hash: 47736bb9c8a317c5b183c45a3f7e21942759cd108bb1bbf7c59e9a160a17f1cd
fetched_at: '2026-06-28T22:38:01.116423+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - BackOffice Linha Protheus - SIGAFIN - MILE - Importação
type: support-article
updated_at: '2023-12-28T08:45:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20124950609815-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-MILE-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20124950577431) Tempo aproximado para leitura: **05:00 min** **Dúvida**Realizar a importação de títulos pagos através do MILE?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Não seria aconselhado efetuar o procedimento através do MILE pois o cliente necessita migrar informações antigas de outro sistema para o PROTHEUS, como a nova versão efetua gravações nas tabelas **FK´s** orientei o cliente a utilizar o MILE somente para popular as tabelas de Origem, no caso as tabelas **SE1, SE2 e SE5** contendo todos os campos Obrigatórios preenchidos, após essa importação, orientei o cliente a executar o Migrador Offline para que o sistema efetue a gravação das **FK´s** conforme a origem. Para utilizar corretamente o migrador solicito que verifique os níveis de compartilhamento antes pois o compartilhamento das tabelas **FK´s** deverão ser idênticos a **SE5** conforme link abaixo.

[Reestruturação da Tabela SE5](https://tdn.totvs.com.br/pages/releaseview.action?pageId=203760476)

Migrador offline: 

O migrador offline - **FINXSE5** é sim para Migrar os registros da tabela **SE5** para as tabelas **FK's,** atualmente o Protheus 12 já possui uma Migração Online que ao realizar as movimentações bancárias (**SE5**) automaticamente os registros são incluídos também nas tabelas **FK's** seguindo a origem, ou seja, todas as movimentações realizadas pela rotina de baixa do Contas a Receber da tabela **SE1** também devem estar na **FK1**, assim como as movimentações da rotina de baixa do Contas a pagar da tabela **SE2** vão para a **FK2**, esse novo modelo de tabelas está sendo implantado para poder melhor organizar as movimentações bancárias e obter melhores relatórios do sistema.

A tabela SE5 controla a migração pelos campos: **E5\_TABORI, E5\_MOVFKS e E5\_IDORI.**

O FINXSE5 é utilizado quando se trata da migração do Protheus 11 para o Protheus 12

Para efetuar a migração off-line dos registros da tabela **SE5 -** ***Baixas e Movimento Bancário,*** para a nova estrutura de tabelas da família **FKx**,é necessário seguir os passos abaixo:

1) Para executar o *wizard* de migração, adicione a rotina ***FINXSE5.***

2) Execute a rotina. Será exibida a tela do *wizard.*

3) Selecione a opção **Perguntas** e informe o range de datas desejado. Este range define o período de movimentos da tabela **SE5** que serão migrados.

4) Confirme a execução do processamento.

**Saiba mais**

[Reestruturação da Tabela SE5](https://tdn.totvs.com.br/pages/releaseview.action?pageId=203760476)
