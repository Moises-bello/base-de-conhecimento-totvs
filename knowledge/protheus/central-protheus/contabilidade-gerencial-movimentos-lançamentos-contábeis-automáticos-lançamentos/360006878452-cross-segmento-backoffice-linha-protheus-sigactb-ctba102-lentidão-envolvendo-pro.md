---
article_id: 360006878452
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: f463d0106807ed9f8c3b831706f3a7b21c69c5167c35a034922ef7948490a83b
fetched_at: '2026-06-28T22:40:32.323502+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Lentidão envolvendo
  processos de contabilização ou atualização de saldos contábeis
type: support-article
updated_at: '2024-06-10T17:33:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006878452-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Lentid%C3%A3o-envolvendo-processos-de-contabiliza%C3%A7%C3%A3o-ou-atualiza%C3%A7%C3%A3o-de-saldos-cont%C3%A1beis
---

**Dúvida**O que devo avaliar para casos de Performance na execução de processo contábil?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Orientação  
Para avaliar a melhoria de performance, realize as validações conforme abaixo:

É importante verificar um passo por vez, pois cada um individualmente pode gerar ganho de performance.

Avalie se as situações abaixo: 

A) Lentidão em processos de contabilização ou Atualização de Saldo:

=> As tabelas abaixo precisam obrigatoriamente possuir o mesmo modo de compartilhamento.

CTE - Moeda X Calendário  
CTG - Calendário Contábil  
CQD - Bloqueio do calendário Contábil  
CTO - Moeda cadastrada  
CTP - Cambio

O parâmetro [MV\_CTBCACH -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000666227-MP-SIGACTB-Como-funciona-o-cache-no-ambiente-cont%C3%A1bil-?source=search)foi criado para atender a rotina Lançamento Contábeis Automáticos(CTBA102), ele indica se o calendário contábil, moeda, câmbio e as entidades contábeis (Plano de Contas, Centro de Custos, Item Contábil e Classe de Valor) devem utilizar as informações em cachê, a fim de otimizar a performance.

Se diferentes será necessário o ajuste do compartilhamento da tabela CQD, deixando igual a CTG 

No primeiro acesso você não sentirá ganho de performance, isso porque a tabela CQD será carregada respeitando o modo de compartilhamento correto, mas após o segundo acesso a performance será restabelecida.

Verifique o [compartilhamento completo para o modulo **SIGACTB)**](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB) exemplo as  tabelas de movimento [CT2,CQ0,CQ1(..)CQ9, CTC,CTF e tabela de cadastro](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)CTD,CTH, CTT

B) Lentidão no Reprocessamento de Saldos (Consumo de espaço em disco)=> Criar parâmetro **MV\_CTB190D** e parametrizar como "F" (False)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=271661635>

O tamanho dos campos "Centro de Custo", "Item Contábil" e "Classe Valor" em SIGACFG/ Base de dados/ Dicionário/ Base de dados/ Dicionário de Dados/ Grupo de campos, devem ter o mesmo tamanho.

Orientações referentes ao tamanho das entidades estão disponíveis nos links:

**[ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search)**

**[Alterar o tamanho do campo código das entidades contábeis adicionai](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)[s](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)**

* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema

**OBS:** Se utiliza a rotina CTBA193 torna-se desnecessário o reprocessamento dos saldos contábeis, o que impactará no consumo de espaço em disco.

C) Lentidão na impressão do relatório **Razão Contábil (CTBR400)**

Configurar o parâmetro **MV\_CTBRAZB = .T.**  
Se estiver configurado como .T. irá criar o arquivo temporário do relatório Razão Contábil (CTBR400) no banco de dados. Irá também criar procedures no banco de dados para popular essa tabela temporária.  
Se o parâmetro não existir ou estiver parametrizado com .F. , fará tudo local.

Se não existir criar o parâmetro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057766313)

**D) Lentidão ao emitir relatórios**

1 - Acesse a rotina CTBA170 - Valida Plano de Contas.  
2 - Preencha os parâmetros.  
  
O sistema emite o relatório com as inconsistências do Plano de Contas, sendo necessário efetuar o ajuste. Após isso validar novamente a emissão do relatório CTBR040 - Balancete Modelo 1.

**Saiba mais:**

<http://tdn.totvs.com/display/public/PROT/CTB0066_Balancete_em_looping>

Solicito que verifique o cadastro das contas (CT1) que estão sendo informadas  no range ao emitir o relatório, realize a mesma analise CTT,CTD e CTH  
- veja se as entidades superiores estão amarradas corretamente (CT1\_CTASUP)  
Ex:  
1 sintética Ativo CT1\_CTASUP = Não possui entidade superior  
11 sintética Ativo circulante  CT1\_CTASUP = 1  
111 Sintética Ativo Disponível  CT1\_CTASUP= 11  
11101 Sintética Caixa CT1\_CTASUP =111  
11101001 Analítica CAIXA  CT1\_CTASUP  = 11101

**E) Lentidão ao Emitir relatórios com visão gerencial**

Realize um teste utilizando modelo de visão gerencial

* **[Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-MP-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial?source=search)**
* **[Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)**

**F) Lentidão ao Gerar ECD ou ECF**

* [Habilitar procedures dinâmica na geração da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search)
* [TABELAS ECD E ECF COMPARTILHAMENTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)
* [MP-SIGACTB: ECD/ECF LIMPEZA TABELA CSB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-MP-SIGACTB-ECD-ECF-LIMPEZA-TABELA-CSB?source=search)

**G) Execute o Diagnóstico**

* Execute o  [**\*Diagnóstico de Dicionário\***](https://tdn.totvs.com/pages/releaseview.action?pageId=725728577)**pois ele p**ermite fazer uma verificação na base em busca de possíveis erros que podem causar problemas na base ou impedir a correta execução de rotinas de atualização , como UPDDISTR por exemplo. Utilizando a rotina de Diagnostico é possível identificar problemas de integridade para uma tabela especifica em sua base de dados , que podem estar ocasionando erros.

**- Integridade SX3 (Campos) x SXG (Grupo de campos)  
- Integridade SX1 (perguntas) x SXG (grupo de campos)  
- Integridade SX3 x tabela física  
- Integridade SX3 (campos) x SIX (índices)  
- Integridade SIX (índices) x tabela física  
Para correção do tamanho dos campo veja: [Como alterar o tamanho de campos via configurador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)**

* Shift+F6 >Avançar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17854960914839)

[Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus?source=search)

[Como desativar customizações via Rpo Custom](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6449793366039-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-desativar-customiza%C3%A7%C3%B5es-via-Rpo-Custom)
