---
article_id: 38618849705879
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f9b3abf4a0be1761d9da126a96d9e851ac4a1a250652ae6e9793556e9b386c2a
fetched_at: '2026-06-28T22:38:54.280249+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ajuste da Numeração
  do Campo D3_DOC por Customização do campo
type: support-article
updated_at: '2026-06-19T15:41:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38618849705879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ajuste-da-Numera%C3%A7%C3%A3o-do-Campo-D3-DOC-por-Customiza%C3%A7%C3%A3o-do-campo
---

O artigo explica que no campo D3\_DOC do sistema SIGAEST a numeração dos documentos segue a maior numeração registrada, somando um, podendo gerar numerações indevidas. O sistema prioriza numeração manual, e a TOTVS recomenda usar funções customizadas para controle de numeração, apresentando um exemplo de função para evitar conflitos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38618825652375) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
No campo de código do documento (D3\_DOC) foi inserida uma numeração indevida e agora o sistema está dando continuidade à ela nos novos documentos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Causa**  
Conforme detalhado na documentação [**Controle de numeração D3\_DOC**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34841866033175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Controle-de-numera%C3%A7%C3%A3o-D3-DOC) a numeração do documento sempre vai pegar a maior numeração já registrada na tabela e somar um.

Ou seja, se você possui uma numeração "A00001" e uma numeração "000030" na tabela SD3, a próxima numeração sugerida pelo sistema será a "A00002", porque os códigos com letras são considerados maiores que os números.

**Solução**  
Um ponto importante é que, apesar da sugestão da numeração realizada pelo sistema, caso o usuário preencha a numeração manualmente o sistema dará prioridade ao que foi digitado:

```
cDocumento := IIf(Empty(cDocumento), NextNumero("SD3", 2, "D3_DOC", .T.), cDocumento)
```

Dessa forma, existe a possibilidade de inserir uma função de usuário no Inicializador padrão do Campo D3\_DOC.

Alguns clientes utilizam a função [**GetSXENum**](https://tdn.totvs.com/x/NYFzAQ), que não existe por padrão no campo de Numero do Documento (D3\_DOC), porém algumas particularidades não são tratadas pela função.

A orientação da TOTVS, caso necessite alterar a forma de sugestão da numeração, é que seja utilizada uma função customizada para tratar o controle de numeração.

Abaixo indicamos um exemplo de função:

**Atenção!** **Trata-se apenas de um exemplo, caso necessite customizar, solicite o acompanhamento de seu analista programador.**

```
#Include 'TOTVS.ch'  
  
User Function NextSD3Doc()  
Local cNum := GETSXENUM("SD3","D3_DOC")  
  
DbSelectArea("SD3")  
SD3->(DbSetOrder(2))  
While (DbSeek(xFilial("SD3")+cNum))  
ConfirmSX8()  
  
cNum := GETSXENUM("SD3","D3_DOC")  
Enddo  
  
DbCloseArea()  
RollbackSx8()  
Return cNum
```

Para assuntos sobre customizações TOTVS, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de pontos de entrada e rotinas automáticas documentadas  no portal TDN para uso no produto padrão.  
Estas documentações possuem exemplos de utilização previamente testados, caso utilize estes e o resultado seja diferente do documentado ou apresente falha, caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time Hub Plataformas ([hub.plataformas@totvs.com.br](mailto:hub.plataformas@totvs.com.br)).

Esta equipe oferece os serviços de criação e manutenção de fontes Protheus, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
