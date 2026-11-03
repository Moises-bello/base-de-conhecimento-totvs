---
article_id: 360035319633
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 92ae3df65b6d5fb80e17cb5c2d8da9276b5cb7e9859996fd1bf41d536167e8ce
fetched_at: '2026-06-28T22:40:40.290755+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF Simulação Apuração
  IRPJ CSLL no TAF (TAFA433)
type: support-article
updated_at: '2022-06-02T17:38:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433
---

**Dúvida**

Apuração IRPJ CSLL Simulação da Apuração no TAF  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

**Necessário executar** :  **[Lalur /Lacs - Cadastro, apuração e integração com o E](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-Lalur-Lacs-Cadastro-apura%C3%A7%C3%A3o-e-integra%C3%A7%C3%A3o-com-o-ecf?source=search)CF**

## **TAFA433 Objetivo(Simulação)**

Este serviço tem como objetivo mostrar como o cálculo do tributo será/foi realizado de forma detalhada e diagramada. A exibição é feita, demonstrando-se todos os valores finais e intermediários do processo de cálculo, de acordo com o tributo e a forma de tributação em questão.

## **Definição da Regra de Negócio**

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045276194/mceclip0.png)*

**Cadastro de Evento Tributário**  
  
Será criado o processo "Simulação da apuração" no cadastro do Evento para possibilitar o usuário verificar como será o comportamento do evento  tributário durante a apuração, demonstrando detalhamento os valores e cálculos envolvidos.

O processo solicitará os seguintes parâmetros para execução da simulação.

1. **Evento Tributário 1**: Evento tributário principal para o qual a simulação será executada.
2. **Simulação Comparativa?**: Indica que a simulação será apresentada para dois eventos tributários possibilitando ao usuário visualizar a simulação de forma comparativa.
3. **Evento Tributário 2**: Evento tributário secundário apresentado na apuração em modo comparativa.

   **RN01**

   1. O Evento Tributário tem que ter o mesmo tributo do evento principal;
   2. Se o evento principal for para Filial SCP o evento secundário tem ser para a mesma Filial SCP;
   3. Se o evento principal for para Filial Matriz o evento secundário tem ser para Filial Matriz.
4. **Período**: Identifica o(s) período(s) para o(s) qual(is) a simulação será apresentada.

**Protótipo de tela**

**![](https://tdn.totvs.com/download/attachments/270906240/Param-Simula%C3%A7%C3%A3o.png?version=2&modificationDate=1483964589000&api=v2)**

Após a execução do processo será exibido uma aba de Simulação com os cálculos do período e uma aba com o detalhamento da apuração.

**Protótipo de tela**

**![](https://tdn.totvs.com/download/attachments/270906240/simula%C3%A7%C3%A3o-2.png?version=2&modificationDate=1483720119000&api=v2)**

**![](https://tdn.totvs.com/download/attachments/270906240/simula%C3%A7%C3%A3o-3.png?version=1&modificationDate=1483721756000&api=v2)**

A diferença entre a simulação e o detalhamento está no fato de que a primeira retorna valores totais de cada grupo processado e a memória de cálculo, demonstra o caminho que o sistema percorreu para chegar ao valor devido do tributo, enquanto que na segunda, são apresentados todos os itens tributários que compõem o Evento Tributário.

**Atenção**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046128813/mceclip1.png)Todos os cálculos serão executados conforme as regras da apuração [PCREQ-9495\_Encerramento\_Período\_Apuração](http://tdn.totvs.com.br/pages/viewpage.action?pageId=244428177)

**Tabelas Utilizadas**

· T0N - Cadastro do Evento Tributário

· T0O - Itens do Evento Tributário

· CWV - Cadastro de Período de Apuração

· CFR - Identificação da Conta na Parte B do e-Lalur e do e-Lacs

· T0S - Conta da Parte B

· LE9 - Tributos da Conta da Parte B

· T0T - Lançamentos na Conta da Parte B

· LEE - Grupos da Forma de Tributação

· LEC - Lançamento Manual Evento Tributário

· CWX - Detalhamento da Apuração

· T50 - Docs Arrecadação Per Apuração

· C0R - Documentos Arrecadação

· T0U - Proc Jud/Admin Lan Cta Parte B

· T0J - Cadastro de Tributos

<https://tdn.totvs.com/pages/viewpage.action?pageId=270905643>

<https://tdn.totvs.com/pages/releaseview.action?pageId=248578386>

# Conteúdos Relacionados

* [Cadastro de Tributos](http://tdn.totvs.com/display/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12);
* [Cadastro de Eventos Especiais](http://tdn.totvs.com/display/TAF/Cadastro+de+Eventos+Especiais+-+TAFA443+-+TAF+-+P12)

Veja mais :

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)

[MP-SIGACTB - ECF :TAFA433 apuração  de IRPJ e CSLL o TAF saldo "Imposto Devido Meses Anteriores" cumulativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035535754-MP-SIGACTB-ECF-TAFA433-apura%C3%A7%C3%A3o-de-IRPJ-e-CSLL-o-TAF-saldo-Imposto-Devido-Meses-Anteriores-cumulativo-?source=search)

[MP\_SIGACTB :TAF-Controle do PAT na Parte B do LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-MP-SIGACTB-TAF-Controle-do-PAT-na-Parte-B-do-LALUR?source=search)

[MP - Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)
