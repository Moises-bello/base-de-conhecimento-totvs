---
article_id: 360051194493
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 7fe45c9abad20a8d568b588b591efa8a5f28619c0d8d8142c95ea09b59ea9b5e
fetched_at: '2026-06-28T22:40:47.388187+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - L210 SEM CENTRO
  DE CUSTO
type: support-article
updated_at: '2024-05-20T15:06:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051194493-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-L210-SEM-CENTRO-DE-CUSTO
---

**Dúvida***Registro L210 sem centro de custo*

**Ambiente**Protheus Contabilidade Gerencial -A partir da versão P11  
  
**Solução**

* **[Arquivo modelo visão gerencial L210](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312)**
* **[Necessário Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)**
* [**Exemplo de uso e validação da função SaldoConta | Bloco L210, a formula só deve ser utilizada  quando desejar considerar o saldo anterior, caso não seja necessário considerar o saldo anterior Não deve informar formula na visão gerencial**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008886811671-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Exemplo-de-uso-e-valida%C3%A7%C3%A3o-da-fun%C3%A7%C3%A3o-SaldoConta-Bloco-L210?source=search)
* Verifique o cadastro da Visão gerencial L210 não informei visão gerencial o centro de custo

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077261894)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078391433)**

* Emita relatório Balancete (CTBR040) Informando a visão gerencial de L210 , para conferencia do saldo que seja gerado no TAF

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23608395545879)**

* Conta 41101001 não possui centro de custo amarrado

***![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078392633)***

* Conta 41101002 não possui centro de custo amarrado

***![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077262874)***

* Veja os Lançamentos da contas que foram amarradas a visão gerencial

***![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078395773)***

* Verifique como o  parâmetro  abaixo foi preenchido

***![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078399533)***

***![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077269674)***

***![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077269714)***

* Solicito que verifique as***[Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)***

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077271714)

**Para conciliação dos saldos**

* Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial

* Verifique a tabela CSD os registros foram gerados

***![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078400093)***

* Verifique o saldo CSE os registros foram gerados

***![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078400413)***

* Através do gerenciado de integração veja se dados foram gerados

***![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077269814)***

* Através da tabelas TAFST1 e TAFST2 verifique se o T088AC foi gerado
* Com base na [estrutura do Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271) verifique a do Bloco T088AB e T088AC.

   -Verifique se a tabela TAFST1 foi alimentada :

  - no registro da conta verifique T088

    \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

       \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

     Ex:

  |T088AB|1|

  |T088AC|32|2500|

  |T088AC|33|1000|

  |T088AC|34|1500|

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077270854)

Com base na [estrutura do Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)  verifique se a estrutura gerada está correta

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078401353)

 Acesse as rotinas abaixo para verificar se os registros foram alimentados:

**Registro L200 - Método de Avaliação do Estoque Final**

* Tabela - CAR (Método Avaliação Estoque Final)
* Registro do Layout TOTVS - **T088AB**
* Rotina - [**TAFA361**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) (Bloco L - Lucro Líquido)

**Registro L210 - Informativo da Composição de Custos**

* Tabela - CAS (Informativo da Comp. de Custos)
* Registro do Layout TOTVS - **T088AC**
* Rotina - [**TAFA361**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) (Bloco L - Lucro Líquido)

***![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077270054)***

* *Ao* gerar o arquivo o sistema gerou o L210

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077278114)***

* Veja estrutura

|L210|32|CUSTO DAS MERCADORIAS REVENDIDAS|2500,00|  
|L210|33|Estoques no Inicio do Período de Apuracão|1000,00|  
|L210|34|Compras de Mercadorias no Mercado Interno|1500,00|

* Definição dos campos com base no manual da receita

L210|: Identificação do tipo do registro.  
|32|: Código da linha.  
|CUSTO DAS MERCADORIAS REVENDIDAS|: Descrição da linha.  
|2500,00|: Valor da linha (R$ 2.500,00).

***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077278674)***

Saiba mais

<http://tdn.totvs.com/display/public/PROT/ECF0004_REGISTROS_L200_L210_NAO_SAO_GERADOS_NO_TXT>

[ERRO "SALDO DOS SERVIÇOS VENDIDOS INFORMADO NO REGISTRO L210 (66) DIFERENTE DO CUSTO DOS SERVIÇOS VENDIDOS NO REGISTRO L300 .."](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025703393-MP-SIGACTB-ECF-ERRO-SALDO-DOS-SERVI%C3%87OS-VENDIDOS-INFORMADO-NO-REGISTRO-L210-66-DIFERENTE-DO-CUSTO-DOS-SERVI%C3%87OS-VENDIDOS-NO-REGISTRO-L300-?source=search)

[REGISTRO L210 É GERADO NO TXT POREM NÃO É EXPORTADO PARA O PGE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033735033-MP-SIGACTB-ECF-REGISTRO-L210-%C3%89-GERADO-NO-TXT-POREM-N%C3%83O-%C3%89-EXPORTADO-PARA-O-PGE?source=search)
