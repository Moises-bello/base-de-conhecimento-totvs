---
article_id: 39269831449879
category: SIGAEST - LEGAIS
content_hash: 4c309405066f2ed780dbd2ffc98307038cf4d9e31c3f64170e73c0e5054553e7
fetched_at: '2026-06-28T22:38:51.527601+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque e Custos (SIGAEST)
  - SPEDFISCAL apresenta lentidão para processar o bloco K
type: support-article
updated_at: '2026-06-17T21:15:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39269831449879-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Estoque-e-Custos-SIGAEST-SPEDFISCAL-apresenta-lentid%C3%A3o-para-processar-o-bloco-K
---

O processamento do arquivo SPEDFISCAL no Protheus pode apresentar lentidão devido a rotinas e procedures desatualizadas, configuração inadequada do parâmetro MV\_BLKMTHR, geração do Bloco H, ou excesso de registros na tabela SD3 com o campo D3\_PERBLK em branco. A solução envolve atualizar fontes, procedures, ajustar parâmetros, avaliar a necessidade do Bloco H e tratar registros antigos, além de coletar logs para análise técnica avançada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39269831437463) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Processamento do arquivo passou a apresentar lentidão . A rotina entra na fase de geração das informações do Bloco K e permanece em processamento contínuo, sem apresentar erros em tela. Porém, o processo que antes era concluído de maneira relativamente rápida saltou para mais de horas de execução.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque e Custos (SIGAEST) - Protheus Release 12.1.33 ou Superior.  
  
**Causa**  
Geralmente a lentidão está atrelada a esses 5 fatores: 1. Rotinas desatualizadas; 2. Procedure desatualizada; 3. Configuração do parâmetro MV\_BLKMTHR; 4. Geração do Bloco H no SPEDFISCAL 5. À quantidade excessiva de registros na tabela **SD3** que possuem o campo **D3\_PERBLK** em branco.  
  
Abaixo estaremos informando com mais detalhes cada ponto mencionado acima e suas instruções.

**Solução**

1. **Rotinas desatualizadas:**  
   Para a geração do SPEDFISCAL, são utilizados diversos fontes sendo esse abaixo essenciais  
   **MATXSPED, PCPXSPED, SPEDXFUN, SPEDFISCAL**  
     
   É de extrema importancia mantê-los atualizados, pois os mesmos estão sempre contando com melhorias pontuais e de performance, caso note que seu ambiente esta desatualizado, por favor , realize também um teste em ambiente de Homologação com as atualizações a seguir:

   [- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
   - [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
   - [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
   - [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
   - [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
   - [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)  
   Obs: Aplicar após backups e validar primeiro em ambiente teste.
2. **Procedure desatualizada:**  
   A procedure é um conjunto de comandos SQL armazenado no banco de dados para realizar tarefas específicas repetidamente, sem necessidade de retornar um valor diretamente ao ADVPL otimizando o desempenho e execução da rotina.   
     
   Após avaliado o as atualizações das rotina verifique se a procedure 14 esta devidamente atualizada em seu ambiente.  
   Possuir a mesma desatualizada ou desinstalada, não impede a execução da rotina, mas pode causar um impacto significativo no seu tempo de execução, segue abaixo uma documentação de apoio.  
   [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel?source=search)
3. **Configuração do parametro MV\_BLKMTHR:**  
   Visando um ganho de performance, o time de produto desenvolveu o parâmetro de threads. Esse parametro habilita o processamento multi-threads está limitado ao **máximo de 20 threads nesse processo**. A alteração da quantidade de threads deve ser feita com critério, **pois pode impactar na performance do sistema como um todo, pois depende da infraestrutura que o suporta.** Saiba mais na documentação abaixo:  
   [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Parâmetro de threads para ganho de performance](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014701152-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Par%C3%A2metro-de-threads-para-ganho-de-performance)
4. **Geração do Bloco H no SPEDFISCAL:**  
   A geração do Bloco H geralmente ocorre para as empresas junto a entrega fiscal do periodo de Fevereiro, dentro do mês de Março, devido a ser necessário a geração de mais informações é normal ocorre um aumento no tempo de processamento.  
     
   Devido a esse ao aumento desse tempo, é recomendado que avalie junto ao seu time de fiscal se tem a necessidade desta entrega, e caso não possua é recomenado configurar o pergunte **Gera Inventário** = Não, no momento que esta gerando o SPEDFISCAL.   
   [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Guia do Bloco H do SPED Fiscal no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059965954-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Guia-do-Bloco-H-do-SPED-Fiscal-no-Protheus)
5. **À quantidade excessiva de registros na tabela** **SD3** **que possuem o campo** **D3\_PERBLK** **em branco:**  
   O processamento do arquivo SPED no Protheus também pode apresenta lentidão devido à grande quantidade de registros na tabela SD3 com o campo D3\_PERBLK em branco, no comportamento padrão do sistema, a cada mês em que o SPED é gerado, o campo D3\_PERBLK é populado com a data da geração (exemplo: 112025).   
     
   Quando o cliente está iniciando as gerações, efetuando trocas de layout ou possui uma base histórica extensa não tratada, o sistema encontra milhares de registros antigos com o campo em branco e tenta analisá-los indevidamente, o que gera o gargalo de performance no processamento e causando análise indevida e gargalo.   
     
   Existem duas formas possíveis para superar este cenário:

   **Primeira opção:** Realizar a geração mensal do SPED dos meses anteriores; dessa maneira, o próprio processamento da rotina preencherá os campos automaticamente.

   **Segunda opção:** Avaliar, junto a um DBA ou analista in loco, a localização dos campos em branco por meio de um filtro que englobe todos os registros antigos com o campo D3\_PERBLK vazio.

   **Exemplo:** Se estiver realizando a geração de Fevereiro de 2026, deve-se aplicar este tratamento para os dois períodos anteriores — neste caso, de Dezembro de 2025 para trás.
6. **Procedimento Avançado:** Caso a lentidão persista mesmo após analisado e corrigido os pontos acima, será necessário coletar evidências simultâneas para análise técnica. Para isso configure o parâmetro **MV\_BLKMTHR** com o valor **1** e gere os seguintes arquivos:

   1. Log Profiler limpo (`console.log`) englobando o processamento do Bloco K.  
      [LogProfiler - Como configurar a execução](https://tdn.totvs.com/x/J1IXEQ)
   2. DbTrace da execução   
      [Como gerar o Log DbTrace para monitorar performance?](https://tdn.totvs.com/x/9eRhE)
   3. Tabela de logs **CV8** sem filtros, para mapear quais registros exatos estão onerando o tempo.
   4. Inspetor de objetos para analisarmos as datas de todos os fontes do SPED e artefatos envolvidos no processo;
   5. o ID da Central de Diagnóstico, segue abaixo uma documentação de como efetuar a extração:  
      [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

**Saiba mais:**  
[SIGAEST - Guia do Bloco H do SPED Fiscal no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059965954-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Guia-do-Bloco-H-do-SPED-Fiscal-no-Protheus)  
[*Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
