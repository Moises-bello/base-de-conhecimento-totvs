---
article_id: 6473235843351
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 70892da90b5c4c070f25d1b4fae5a83c4b64e99c0ba10f719d56f770b9b1f82a
fetched_at: '2026-06-28T22:40:52.716796+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Lentidão na
  exportação da ECD
type: support-article
updated_at: '2023-05-18T13:27:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6473235843351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Lentid%C3%A3o-na-exporta%C3%A7%C3%A3o-da-ECD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida:**  
Como melhorar a performance na geração da ECD ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - SIGACTB- a partir P12.1.33  
  
**Solução**

* **[Travamento signatários ao gerar a ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14677826030615-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Travamento-signat%C3%A1rios-ao-gerar-a-ECD?source=search)**
* Para ganho de performance, as revisões de teste ou antigas (CTBS001) tanto da ECD quanto da ECF, podem ser excluídas com a finalidade de liberar espaço nas tabelas do sped (tabelas CSs) e no banco.  
  Foi criado o parâmetro MV\_CTBDLRV,  que após ser ativado deletará os registros de todas as tabelas das revisões fisicamente da base de dados.  
  **<https://tdn.totvs.com/pages/releaseview.action?pageId=682055908>**Caso o problema de performance seja devido o volume de dados existente nas tabelas CS veja: [ECD/ECF LIMPEZA TABELAS CS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-ECF-LIMPEZA-TABELA-CSB)
* A rotina também possui uma procedure dinâmica   
  O parâmetro **[MV\_CTBSPRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search)** permite habilitar ou desabilitar a procedure dinâmica no processo de escrituração contábil do ECD.  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=549503023>
* Melhoria de performance para geração do arquivo txt.  
  Ponto de entrada desenvolvido na rotina CTBSTXT com o objetivo de alterar o valor do cache de geração do arquivo texto na rotina de Escrituração Contábil.  
  <https://tdn.totvs.com/display/public/PROT/DT_PE_CTBTXCACHE_Arquivo_Texto>  
  obs. Definição do cache conforme ambiente e estrutura de cada cliente.
* A partir da release P12133: Emita o relatório do validador ecd, que temos no módulo (CTBS480) e faça uma pré analise das validações do PGE e analise de estrutura do protheus. <https://tdn.totvs.com/pages/releaseview.action?pageId=665275974>

* A rotina de  **[\*Diagnóstico de Dicionário\*](https://tdn.totvs.com/pages/releaseview.action?pageId=725728577)** Permite fazer uma verificação na base em busca de possíveis erros que podem causar problemas na base ou impedir a correta execução de rotinas de atualização , como UPDDISTR por exemplo. Utilizando a rotina de Diagnostico é possível identificar problemas de integridade para uma tabela especifica em sua base de dados , que podem estar ocasionando erros

- Integridade SX3 (Campos) x SXG (Grupo de campos)  
- Integridade SX1 (perguntas) x SXG (grupo de campos)  
- Integridade SX3 x tabela física  
- Integridade SX3 (campos) x SIX (índices)  
- Integridade SIX (índices) x tabela física

Para correção do tamanho dos campo veja: [Como alterar o tamanho de campos via configurador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)

* verifique o cadastro das contas (CT1) que estão sendo informadas  , realize a mesma analise na tabela CTT   
  - veja se as entidades superiores estão amarradas corretamente (CT1\_CTASUP)  
  Ex:  
  1 sintética Ativo CT1\_CTASUP = Não possui entidade superior  
  11 sintética Ativo circulante  CT1\_CTASUP = 1  
  111 Sintética Ativo Disponível  CT1\_CTASUP= 11  
  11101 Sintética Caixa CT1\_CTASUP =111  
  11101001 Analítica CAIXA  CT1\_CTASUP  = 11101
* Veja se o [compartilhamento das tabelas CT1, CVD,CVN](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB) estão corretas
* Verifique se o [compartilhamento das tabela](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)s CT2, CTC , CTF ,CQ0...CQ9 estão iguais
* Verifique se o  [compartilhamento das tabelas da ECD estão corretas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)
* Gere um revisão sem informar visão gerencial de Balanço. DRE, e DMPL/DPLA , caso melhore a performance sugiro :  
    
  - Realize um teste com novo modelo de [Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018601871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Onde-est%C3%A3o-disponibilizados-os-modelos-de-plano-referencial-e-Vis%C3%A3o-Gerencial-?source=search)  
  -Verifique se o [Compartilhamento de tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search) CTS,CVE, CVF estão corretas
