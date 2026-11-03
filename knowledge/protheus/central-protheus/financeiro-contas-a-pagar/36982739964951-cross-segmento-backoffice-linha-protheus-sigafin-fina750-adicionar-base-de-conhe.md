---
article_id: 36982739964951
category: Financeiro - Contas a Pagar
content_hash: 467bf6d170b0a1964b7475dee64940610b2e1a668fdf9f0a98fee41b5abb21ef
fetched_at: '2026-06-28T22:38:08.336420+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA750 - Adicionar
  base de conhecimento na rotina de funções não está carregando as informações.
type: support-article
updated_at: '2026-03-12T20:08:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36982739964951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA750-Adicionar-base-de-conhecimento-na-rotina-de-fun%C3%A7%C3%B5es-n%C3%A3o-est%C3%A1-carregando-as-informa%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36982739951383) Tempo aproximado para leitura: **00:00:20 min**  
  
**Dúvida**  
Ao acessar o Banco de Conhecimento de Títulos a Pagar (FINA050) pela rotina de Funções do Contas a Pagar, utilizando a função MSDOCUMENT, as informações cadastradas não são exibidas.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA750 - Todas as versões  
  
**Solução**  
A rotina FINA750 não disponibiliza a opção "Banco de Conhecimento". Caso queira inclui-la, via ponto de entrada, segue abaixo um exemplo de implementação:

A integração com o **Banco de Conhecimento** nas rotinas de **Contas a Pagar e Contas a Receber** é realizada por meio da função padrão `MsDocument()`, utilizando a **tabela FK7** como entidade de relacionamento para os documentos.

Não é recomendado utilizar diretamente as tabela **SE2** para armazenamento de anexos.

Cabe destacar que a função `MsDocument()` não é exclusiva dos pontos de entrada **F050ROT()** e **FA750BRW()**. Entretanto, é responsabilidade da customização garantir que o registro esteja corretamente posicionado na **tabela FK7**, obtendo um **RECNO válido**, antes de realizar a chamada da função `MsDocument()`.

A seguir, apresenta-se um exemplo de utilização do **Ponto de Entrada** **F050ROT(),** apontando para uma função padrão disponibilizada para uso.

EXEMPLO:

```
#Include 'Protheus.ch'
#Include 'FWMVCDEF.ch'
 
User Function F050ROT()
     
    Local aArea   := GetArea()
    Local aRotina := Paramixb[1] // Array contendo os botoes padrões da rotina.
 
    // Tratamento no array aRotina para adicionar novos botoes e retorno do novo array.
    Aadd(aRotina, {"Conhecimento", "FA050MsDoc", 0, 4,} )
     
    RestArea(aArea)
 
Return aRotina
```

Utilização do **Ponto de Entrada FA750BRW** para incluir a opção **Banco de Conhecimento** no menu da rotina **FINA750 – Funções do Contas**, permitindo anexar e visualizar documentos relacionados por meio da **tabela FK**7,customizando o processo.

EXEMPLO:

```
#INCLUDE "TOTVS.CH"

User Function FA750BRW()
	Local aBotao := {}
	Local aArea := GetArea()

	AAdd(aBotao, { ;
		"Banco de Conhecimento_", ; // Título do menu
		"U_MSdoc()", ; // Função associada
		0, 4, 0, NIL;
	})
	RestArea(aArea)

Return aBotao


//Validações do usuário
User Function MSdoc()

	DbSelectArea("FK7")

// Montagem da chave conforme o índice 3 da FK7 para posicionar no RECNO do registro.
// Indice 3 = FK7_FILIAL+FK7_ALIAS+FK7_FILTIT+FK7_PREFIX+FK7_NUM+FK7_PARCEL+FK7_TIPO+FK7_CLIFOR+FK7_LOJA
	POSICIONE('FK7',3,xFilial('FK7')+'SE2'+SE2->E2_FILORIG+SE2->E2_PREFIXO+SE2->E2_NUM+SE2->E2_PARCELA+SE2->E2_TIPO+SE2->E2_FORNECE+SE2->E2_LOJA,'FK7->(RECNO())')

// Abre o Banco de Conhecimento permitindo inclusão e visualização, e enviando o RECNO já posicionado para a função MsDocument
	MsDocument('FK7', FK7->(RecNo()), 4)

Return .T.
```

**SAIBA MAIS**

[**Contas a Pagar - FINA050 - Financeiro - P12**](https://tdn.totvs.com/display/public/PROT/Contas+a+Pagar+-+FINA050+-+Financeiro+-+P12)

[**Funções contas a pagar - FINA750 - Financeiro - P12**](https://tdn.totvs.com/pages/releaseview.action?pageId=266976623)

[**PE FA750BRW - Adição de itens no menu da rotina Funções a Pagar**](https://tdn.totvs.com/pages/releaseview.action?pageId=901940855)

[**FA750BRW - Adição de itens no menu da mBrowse**](https://tdn.totvs.com/pages/releaseview.action?pageId=6071251)
