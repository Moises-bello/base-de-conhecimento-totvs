---
article_id: 34644092874519
category: Materiais - Compras (SIGACOM)
content_hash: 788452d3b10bb16274b469b97d36345e1519f842d3eef0e1bea27bad98dc1a8d
fetched_at: '2026-06-28T22:41:12.774148+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Linha Protheus - Compras - Como melhorar
  a performance da contabilização no compras
type: support-article
updated_at: '2025-09-02T19:58:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34644092874519-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-Compras-Como-melhorar-a-performance-da-contabiliza%C3%A7%C3%A3o-no-compras
---

**Dúvida**  
Melhorar performance na contabilização no módulo de compras.

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Todas as versões

**Solução**  
Para melhorar a performance na contabilização off line do módulo de compras ( rotina CTBANFE ), podemos observar alguns fatores listados abaixo:

**1-) O parâmetro MV\_CNFETHR** habilita a contabilização Off-Line utilizando Múltiplas Threads para acelerar o processamento.

***\*Thread** é um pequeno programa que trabalha como um subsistema independente de um programa maior, executando alguma tarefa específica. Um programa dividido em várias threads é processado mais rapidamente do que um programa monolítico, pois várias tarefas podem ser executadas simultaneamente, compartilhando os recursos do sistema.*

**Importante :**

* O numero máximo de threads para o parâmetro **MV\_CNFETHR**e 30, porem recomendamos testes com valores menores para acompanhar o ganho de performance;
* Pergunta ([Mostra Lançamento Contábil?](https://tdn.totvs.com/download/attachments/268825968/Imagem%2001.png?version=2&modificationDate=1695646023077&api=v2)) deve estar configurada com o conteúdo igual a "NÃO";
* Pergunta ([Aglutina Lançamentos?](https://tdn.totvs.com/download/attachments/268825968/Imagem%2001.png?version=2&modificationDate=1695646023077&api=v2)) deve estar configurada com o conteúdo igual a "NÃO";
* O parâmetro [MV\_PRELAN](https://tdn.totvs.com/download/attachments/268825968/MV_PRELAN.png?version=1&modificationDate=1695646083907&api=v2) deve esta configurado com o conteúdo igual a "D"

Ao executar a rotina de processamento "Contabilização Off-Line - CTBANFE" para contabilizar os movimentos  o campo **F1\_DTLANC SEMPRE** será atualizado com sua data de processamento, mesmo que não seja gerado lançamento contábil na tabela CT2. Esse procedimento é utilizado para evitar reprocessamento indevidos de movimentos já avaliados pela rotina.  
  
Se optar pelo uso de múltiplas threads pra melhoria de performance, não poderá trabalhar com uso schedule  para contabilização. A rotina de contabilização via faturamento, **CTBANFE**, só funciona via schedule, caso ela não esteja configurada para utilizar múltiplas threads.  
  
[**Isso ocorre pois as threads do Schedule (SIGACFG) são diferenciadas das Threads dos módulos do sistema. Então via Schedule, é considerado Threads do Agent e não de parâmetros dos demais módulos.**](https://tdn.totvs.com/download/attachments/268825968/image-2024-1-31_13-45-48.png?version=1&modificationDate=1706719549110&api=v2)

[**Dúvidas na configuração das Threads do Agent (Configurador), contate a Equipe Framework.**](https://tdn.totvs.com/download/attachments/268825968/image-2024-1-31_13-45-48.png?version=1&modificationDate=1706719549110&api=v2)

**2-) O parâmetro MV\_OPTNFE** muda o comportamento de processamento da rotina CTBANFE, pois na montagem da massa de dados para processamento ao invés de ler registro-a-registro a rotina monta uma query (Select) no banco de dados recuperando todos os registros a serem processados (CURSOR).  
Em testes em clientes verificamos um ganho de aproximadamente 30% no processamento da rotina.

**Importante:** Com a mudança do parâmetro é necessária uma revisão geral das LP's.  
  
Passo-a-passo

1. Alterar o parâmetro [**MV\_OPTNFE**](https://tdn.totvs.com/pages/releaseview.action?pageId=6085182) para o conteúdo igual a .T. (Verdadeiro);

2. Realizar uma revisão das LP's abaixo trocando o alias das tabelas pelo nome do cursos "**CTBANFE**":

Lista de LP's disponíveis na rotina CTBANFE

[**LP´s do compras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras-Quais-Lan%C3%A7amentos-Padr%C3%B5es-e-como-funciona?source=search)

Exemplo da troca do alias das tabelas:

* No exemplo vou utilizar o principal lançamento padrão da rotina CTBANFE ( 650 )
* No modo PADRÃO (MV\_OPTNFE = .F.) quando incluímos as LP's informamos nos campos macro-executados o apelido das tabelas utilizadas, por exemplo  " SD1-> "
* No modo performático (MV\_OPTNFE = .T.) devemos obrigatoriamente ajustar as LP's alterando os campos macro-executados para o novo apelido [" **CTBANFE** "](https://tdn.totvs.com/pages/viewpage.action?pageId=349181290)

Você pode utilizar este mecanismo de performance em conjunto com o parâmetro MV\_CNFETHR (Múltiplas Threads);Se os Lançamentos Padrões Offline foram definidos para tratar o apelido “**CTBANFE"** os mesmos não poderão ser utilizados em um processo de contabilização Online.

**3-)** **PERÍODO CONTABILIZADO :**

Contabilização por Período / Documento / Dia, qual o mais performático?  
  
Na parametrização da contabilização off-line da Nota Fiscal de Saída temos três tipos de parametrização “Por Documento”, “Por período” e “Por Dia”.  
Identificamos que o tipo “Por Documento” e “Por Dia” utilizam muito acesso a disco do CTREE/ADS que pode gerar uma pequena queda na performance.  
Recomendamos a utilização da opção “[**Por Período**](https://tdn.totvs.com/download/attachments/268825968/03.%20por%20per%C3%ADodo.png?version=1&modificationDate=1695647405857&api=v2)” que possui maior desempenho no processamento de grandes volumes de contabilização.

***Saíba Mais :***

* [Como habilitar e gerar o LogProfiler para avaliação de desempenho (trace para rotinas ADVPL)](https://tdn.totvs.com/x/h6GFDg)
* [O parâmetro MV\_CTBCATH é amplamente utilizado para otimizar as rotinas de contabilidade](https://tdn.totvs.com/x/qJhc)
* [Criação de campos adicional na tabela CT5 para que seja replicado o conteúdo nas tabelas CT2 e CTK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043003714-MP-SIGACTB-CTBA105-Alimentar-campos-adicionais-na-tabela-CT2-atrav%C3%A9s-das-Integra%C3%A7%C3%B5es-Cont%C3%A1beis)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
