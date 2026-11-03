---
article_id: 360005048472
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: c189289ca7e47b42fd06223392dd29e1cc369e29c1ff0988272c87d988225d6c
fetched_at: '2026-06-28T22:41:04.961025+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Como realizar
  Apuração de resultados dentro do Protheus
type: support-article
updated_at: '2025-05-13T18:59:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus
---

**Dúvida**Como realizar Apuração de resultados (CTBA211) dentro do Protheus?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial - Versão 12

**Solução**

Antes de executar a rotina de apuração de resultados, realize:

* [APURAÇÃO DE RESULTADO :O SISTEMA NÃO ESTA ZERANDO AS CONTAS DE RECEITA E DESPESA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046954954-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DE-RESULTADO-O-SISTEMA-N%C3%83O-ESTA-ZERANDO-AS-CONTAS-DE-RECEITA-E-DESPESA?source=search)
* A atualização do seu ambiente conforme a documentação: [Atualização do Ambiente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000043507)
* Aplicar o pacote do link [Pacote de Atualização - Contabilidade Gerencial + Dicionário +Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)
* Realizar a [**atualização das procedures**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)
* Realize o ajuste no compartilhamento das tabelas conforme documentação: [Compartilhamento das Tabelas Contábeis](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* Ajuste o tamanho das entidades contábeis conforme a documentação: [Procedimento para alteração do tamanho das entidades contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=6068430)
* Ajuste o tamanho das casas decimais conforme a documentação: [Ampliação da quantidade de casas decimais em outras moedas](http://tdn.totvs.com/pages/viewpage.action?pageId=6068431)
* E avalie a documentação: [Ampliação do Código de Entidades](http://tdn.totvs.com/pages/viewpage.action?pageId=6068420)

#### **Importante:** 📢

Caso não seja executado um dos passos mencionados, o sistema poderá **não** realizar o processo de encerramento e/ou retornar erro ao usuário no momento da execução. Desta forma, é imprescindível a execução da atualização e dos ajustes dos dicionários conforme descrito acima.

* Conceito sobre e parâmetros para a execução da Apuração de Resultado: [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=334338459)

Após realizar os ajustes mencionados, efetue o reprocessamento completo dos saldos. Em seguida, acesse a rotina **Apuração de Resultados (CTBA211)** e siga o **CheckList** abaixo para garantir a execução correta do processo:

1. Verificar se a rotina utilizada é a **CTBA211**, pois a **CTBA210** foi descontinuada. É possível verificar qual está em utilização por meio do parâmetro **MV\_CTBLPV;**
2. Verifique se a rotina **CTBA211** está atualizada de acordo com o portal do cliente;
3. Parametrização para as entidades contábeis (**conta contábil** / **c.custo** / **item contábil** / **classe de valor**) no pergunte da rotina.  
   3.1 = Não utilize de **Branco** a **zzz** na parametrização ao realizar a [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)  
   3.2 = Insira sempre o intervalo a ser apurado, por exemplo: Conta **3** até **49999**. (contas contábeis)  
   3.3 = Verifique se a conta de apuração está sempre fora desse intervalo de apuração. **Exemplo**: Conta 5   
   3.4 = Isto serve para as entidades **C.custo** / **Item** / Classe de valor, a entidade de apuração não pode estar no intervalo a ser apurado.  
   3.5 = Caso **não utilize entidades** em sua apuração, mantenha a pergunta em branco.  
   3.6 = Caso a apuração for anual **não deve ser utilizado o conceito de conta ponte**.

**Na apuração de LUCROS E PERDAS considere o seguinte:  
  
Apuração para controle gerencial : Apuração com conta PONTE**

1) **APURAÇÃO MENSAL , BIMESTRAL , TRIMESTRAL** até mês 11 (Sem encerrar, ou seja sem zerar os saldos das contas de despesas e receitas ), em Dezembro executar o Item II.

* [Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-com-Conta-Ponte-Contas-de-Resultados-e-Encerramento?source=search)
* [Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-com-Conta-Ponte-Contas-Transit%C3%B3rias-e-Encerramento?source=search)

**Observação ⚠️:** O sistema considera no saldo conta a conta de Despesas e Receitas, e realiza um lançamento deste saldo na Conta Ponte , contra a conta de Apuração de Resultado ,  
Execute este processo até o mês de Novembro.

Ao trabalhar com apuração Mensal, Bimestral ou Trimestral deve-se trabalhar com Conta Ponte.

**Apuração de resultado : Apuração Sem conta PONTE**

**1) Apuração Trimestral : Apuração Sem conta PONTE**

\*\*Apuração Trimestral – (as contas são zeradas, ou seja  zerar os saldos das contas de despesas e receitas)

* [Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

**2) Apuração Anual : Apuração Sem conta PONTE**

\*\*Apuração Anual – ( as contas são zeradas, ou seja  zerar os saldos das contas de despesas e receitas )

* [Exemplo - Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

#### **Importante:** 📢

**O Encerramento do exercício CTBA400, fecha somente o calendário contábil, impedindo após o encerramento novos lançamentos contábeis neste período encerrado, porém os relatórios são emitidos normalmente.**

Links de documentação:

* [HELP: Apuração de Resultado](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba211_apuracao_de_resultados.htm)
* [HELP: Considerar Entidades](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba211_considera_entidades.htm)

Ao termino da apuração, execute o reprocessamento de saldos completos

Realize a extração dos relatórios **contábeis** (Balancete e Razão) e verifique se todas as contas de resultado foram zeradas. Caso não estejam zeradas, proceda com o estorno da apuração e realize novamente a apuração.

Se atente ao fato da rotina de apuração considerar as outras entidades contábeis (custos), portanto, se estiver utilizando as entidades com a finalidade de controle contábil, deve-se zerar também as entidades de custo.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068075073)****Caso queira realizar**  [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR (Clique Aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)

**IMPORTANTE:**A rotina de apuração de resultados pode ser executada em outra empresa / filial, porém é necessário obter o controle sobre a execução em modo multifilial para que não seja possível realizar a apuração de resultados na mesma filial por usuários diferentes, é exibida a mensagem: **Não foi possível excluir o arquivo: "+ "\_LP" + EMPRESA + FILIAL + “AA” (ano com 2 dígitos) Erro - Arquivo em uso ou travado.**

Ao processar a rotina de **Apuração de Resultados** não é possível digitar movimentos contábeis neste período, pois a rotina depende dos saldos estáticos no momento da apuração.

Após a apuração de resultados é altamente desejável o bloqueio do calendário a fim de não permitir digitação de lançamentos contábeis retroativos nas contas de resultado e da conta de apuração, uma vez, que as contas de resultados já foram zeradas.

Tabela **CT2** para o campo **CT2\_DATA** = (data da apuração) e **CT2\_ROTINA** = 'ctba211' não deletados, deve conter os lançamentos para zerar as contar de resultado com o conteúdo **CT2\_DTLP** = (data da apuração)

 Tabelas **CQx**(0, 1, 2, 3, 4, 6, 7, 8 e 9) o campo **CQx\_DTLP** = (data da apuração)  
5.C - Os relatórios "**Razão Contábil** (CTBR400)", " **Balancete**(CTBR040)", "**DRE** (CTBR510)" e "**Balanço Patrimonial** (CTBR500)" das contas de resultado após apuração devem estar com saldo zerados. (considerando que não há saldo remanescente de anos anteriores para as contas)

**Veja mais:**

* Help Online  :[Apuração de Resultados por Movimento](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba210.htm)
* Performance na apuração de resultado: [DT Performance](http://tdn.totvs.com/pages/viewpage.action?pageId=239039851) e [Performance CTBA211](http://tdn.totvs.com/display/PROT/CTB0127_Performance_CTBA211)
* Encerramento do Exercício: [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=334338624)
* Atualização de saldos em fila: [Clique aqui](http://tdn.totvs.com/display/PROT/CTB113_REPROCESSAMENTO_SALDOS_POR_FILA_P12)
* Apuração de resultado em Vídeo (How to): [Clique aqui](https://www.youtube.com/watch?v=_Z35wE42wHI&t=7s)
* Verifique o tamanho dos campos "Conta contábil" ,"Centro de Custo", "Item Contábil" e "Classe Valor"   
  [MP - SIGACTB - ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)e [GRUPO DE PERGUNTAS CTB211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)
* Os campos **CTT\_CUSTO, CTD\_ITEM, CTH\_CLVL e CT1\_CONTA** consultado via **APSDU** na tabela **SX3** devem ter o mesmo tamanho do informado no respectivo grupo de campos.

[CTBA211 Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

[CTBA211 Exemplo - Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

[CTBA211 Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-Transit%C3%B3rias-e-Encerramento?source=search)

[CTBA211 Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-de-Resultados-e-Encerramento?source=search)

* [CTBA211 :1º Apuração com Conta ponte e 2º sem Conta : Não é permitida duas apurações para o mesmo período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033694854-MP-SIGACTB-CTBA211-1%C2%BA-Apura%C3%A7%C3%A3o-com-Conta-ponte-e-2%C2%BA-sem-Conta-N%C3%A3o-%C3%A9-permitida-duas-apura%C3%A7%C3%B5es-para-o-mesmo-per%C3%ADodo?source=search)
