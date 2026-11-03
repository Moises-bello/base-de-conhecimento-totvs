---
content_hash: f3150663864f8609cadb1afe16460f1e3585a3c6ac30bf0d3df378a7c06e3b05
fetched_at: '2026-06-29T00:10:03.784572+00:00'
page_id: '452719155'
product: rm
source: tdn-rm
title: Roteiro Relatório LTCAT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719155
version: 4
---

**Roteiro Relatório LTCAT**

---

O Laudo Técnico das Condições Ambientais de Trabalho (LTCAT) tem por objetivo identificar e avaliar os riscos do ambiente de trabalho de acordo com as atividades exercidas pelos trabalhadores, dadas as suas funções e locais de atuação, afim de determinar se estes agentes nocivos têm potencialidade para causar danos à sua integridade física ou à sua saúde.  
   
Sua finalidade é expor ao INSS as condições de trabalho na qual o funcionário esteve exposto, indicando se suas atividades ou operações eram executadas em condições insalubres, ou seja, se estavam expostos a agentes nocivos (físicos, químicos ou biológicos, ou ainda a associação destes) ou não, no intuito de validar a concessão da Aposentadoria Especial.  
   
   
A atualização das informações prestadas deverá ser atualizada anualmente ou quando ocorrer alguma alteração do ambiente de trabalho ou da exposição de agentes nocivos ao trabalhador.  
   
Foi criado o cadastro de CNAE (Acessar: Segurança e Medicina do Trabalho , PPRA | Grau de Risco / Atividade Econômica)que traz as informações de CNAE e sua relação com o Grau de Risco. Neste cadastro não é necessária nenhuma alteração. Para estas classificações se faz necessário acessar o cadastro de Reconhecimento / Avaliação de Risco e informar a devida classificação.  
Foi criada a tabela dinâmica de Tempo de Exposição que por sua vez traz informações baseadas nas definições da Portaria n. 3.311 / 89 cujas classificações:  
*• até 30 minutos por dia = **trabalho eventual;***  
*• até 400 minutos por dia (próximo de 6 horas e meia) = **trabalho intermitente;***  
*• acima de 400 minutos por dia = **trabalho permanente, contínuo ou habitual.***  
**Atenção:**  
 A correta parametrização do sistema é fundamental para correta impressão dos dados.  
   
**Passo 1**  Para a elaboração do LTCAT deverá ser criado o tipo de relatório LTCAT. A opção para cadastro encontra-se em: **Segurança e Saúde Ocupacional | Relatórios | Tipos de Relatórios.**  
   
**Passo 2**  
 Após, é preciso gerar o modelo de LTCAT do tipo de relatório criado, em **Processos | Gerar modelo de LTCAT**.  
 Para conferir se foi gerado corretamente, vá em **Anexos | Itens de Relatório**.  
   
**Passo 3**  
 Em **Segurança e Saúde Ocupacional | Relatórios | Relatórios de LTCAT**, é preciso incluir um novo relatório e o parametrizar na aba *Identificação* conforme sua necessidade de período início e fim. Preencha o *Cód. Tipo Relatório* com o código do relatório LTCAT criado no passo 1.  
 Na aba *Parametrização* inclua os seguintes parâmetros obrigatoriamente de acordo com sua necessidade.

* Coligada (Campo *CODCOLIGADA*)
* Filial (Campo *CODFILIAL*)
* Seção (Campo *CODSECAO*)
* Função (Campo *CODFUNCAO*)

   
**Passo 4**  
 Quanto à *seção* a ser utilizada, em **Segurança e Saúde Ocupacional | Cadastros | Seções**, atente às seguintes situações:

* Campo *Atividade Econômica (CNAE 2.0)* - O mesmo deve estar preenchido com CNAE.
* Aba *Descrição do Local* - Se a mesma está preenchida.
* Aba *Descrição do Ambiente de Trabalho: essa aba foi substituída pelo Cadastro de Ambiente de Trabalho, existente no Totvs Segurança e Saúde Ocupacional.*

 **Observação - CNAE**  
A CNAE, em **Segurança e Saúde Ocupacional | PPRA | Grau de Risco/Atividade Econômica** deve estar cadastrada corretamente, com seu *código* e *Descrição da Atividade Econômica*, sendo o *Grau de Risco opcional. O CNAE informado nesse campo deve estar cadastrado na tabela de CNAE.* 

Ou seja, o CNAE informado no cadastro de seção deverá ter o valor valido disponível no cadastro de GRAU DE RISCO/ATIVIDADE ECONOMICA.

**Passo 5**  
 A *função*, em **Segurança e Saúde Ocupacional | Cadastros | Funções** deve possuir preenchida a:

* Aba *Descrição*.
* Aba *Outras Informações* campo *Objetivo da Função*.

   
**Passo 6**  
 Possuindo as etapas acima realizadas, é possível já gerar o relatório LTCAT. Em **Segurança e Saúde Ocupacional | Relatórios | Relatórios de LTCAT**, vá à aba *Gerar/Visualizar*, gere o relatório e em seguida o visualize.  
   
   
 Para maior detalhamento dos dados a serem extraídos para o relatório, segue informações  dos campos em relação à sua tabela de origem na base de dados:  
   
**Campo 1 – Identificação**  
·          GFILIAL, VCNAEGRAURISCO, PSECAO, PFUNCAO, PFUNC  
   
**Campo 2 – Identificação do Local Periciado**  
·          PFUNCAO, PSECAO  
   
**Campo 3 – Descrição do Ambiente de Trabalho**  
·          PSECAO  
   
**Campo 4 – Descrição das Atividades do Trabalhador**  
Os dados deste campo, depende da forma que foi parametrizado o controle de lotação no sistema:  
            Tipo de Controle Sem Controle ou Função:  
·          PFUNCAO  
   
Tipo de Controle Seção Folha ou Seção em Qualquer Nível  
·          PSECAO  
Tipo de Controle por Quadro de Lotação  
·          VMEMO, VLOTACAO  
   
**Campo 5 – Análise Qualitativa e Possíveis Riscos Ocupacionais**  
·          VPPRAMEDICOES, VPPRARISCOS, VAGENTE  
   
**Campo 6 – Tempo de Exposição aos Riscos**  
·          VAGENTE, VPPRAMEDICOES, GCONSIST, GDINAM  
   
**Campo 7 – Análise Preventiva**  
·          VCATALOGOEPI, VPPRAMEDICOES, VPPRAHISTEPINIVELRISCO, VHISTEPISEGURANCA  
                         
**Campo 8 – Metodologia de Avaliação Ambiental**  
·          VPPRARISCOS, VPPRAMEDICOES, TUND  
                         
**Campo 10 – Técnicas utilizadas:**  
·          VPPRATECNICASMEDICAO, VPPRAMEDICOES  
   
**Campo 11 – Conclusão**  
·          PFUNCAO
