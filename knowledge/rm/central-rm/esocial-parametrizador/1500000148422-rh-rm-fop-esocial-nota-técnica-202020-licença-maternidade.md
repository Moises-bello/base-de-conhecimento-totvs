---
article_id: 1500000148422
category: eSocial - Parametrizador
content_hash: 0c2215df8b7dcb053f4b7c84782f28e1b19f09a451af78ff8964ef1a148de520
fetched_at: '2026-06-28T22:47:06.326325+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Nota Técnica 20/2020 - Licença Maternidade
type: support-article
updated_at: '2025-07-02T17:18:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000148422-RH-RM-FOP-eSocial-Nota-T%C3%A9cnica-20-2020-Licen%C3%A7a-Maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24482152699159) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**  
O que é a Nota Técnica 20/2020 e quais mudanças no produto serão necessárias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - - A partir da 12.1.27.311, 12.1.28.219 e 12.1.29.148  
  
**Solução**  
Em 01/12/2020 foi disponibilizado pelo eSocial a Nota Técnica 20/2020, apontando ajustes no Layout do S-5001 referente ao cálculo de salário maternidade devido à decisão do Supremo Tribunal Federal (STF) sobre o assunto. A decisão indica que é **inconstitucional a incidência de contribuição previdenciária a cargo do empregador sobre o salário-maternidade**.  
  
Em estudo, identificamos que cliente que utilizam o **TAF Full** não precisarão realizar nenhum tipo de atualização. Já clientes que fazem uso do **Middleware** precisarão atualizar o RM conforme *Patches* citados na área **Ambiente** para ajuste do **Relatório Comparativo de INSS**.  
  
Além disso, **todos os clientes RM** devem aplicar os processos abaixo para ajuste da **GPS (Guia de INSS), Folha Analítica e Encargos:**

1. Os eventos com códigos de cálculos de salário maternidade (CC017, CC178, CC371, CC372, CC373 e CC374) deverão ter o parâmetro **Incidência Exclusiva do Segurado** marcado;  
2. Após a alteração realizada no item 1 serão gerados gatilhos do evento **S-1010**. Não é obrigatório o envio desses eventos ao governo, pois terão os mesmos **codIncCP** 21 (Mensal) ou 22 (13º). Assim, caso o usuário não queira enviá-los, poderá excluí-los da fila de eventos;  
3. As rotinas de **Guia de INSS** (GPS), **Folha Analítica** e **Encargos Contábeis** já consideram o parâmetro **Incidência Exclusiva do Segurado**, aplicando no item 1.

**Importante**  
Como não houve nenhuma alteração no Layout do S-1010, não há necessidade de reenvio de eventos para o eSocial. O próprio governo já alterou a forma de cálculo do S-5001, que já está sendo aplicada para todos os eventos enviados a partir de 01/12/2020.  
  
**Saiba mais**  
Para mais informações, acesse:  
     • [Nota Técnica nº 20/2020](https://tdn.totvs.com/pages/releaseview.action?pageId=574891361)  
     • [Guia de INSS (GPS) e Folha Analítica](https://tdn.totvs.com/pages/releaseview.action?pageId=520101874)  
     • [Guia de INSS (GPS) e Folha Analítica 13o. Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=520671442)  
     • [Encargos Contábeis](https://tdn.totvs.com.br/pages/releaseview.action?pageId=532664472)
