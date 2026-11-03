---
content_hash: b5bb65b656633ea249a6b15bc76823adf19917f95be8a910e34556ec321b596d
fetched_at: '2026-06-29T00:10:50.751064+00:00'
page_id: '562966668'
product: rm
source: tdn-rm
title: Bloco Q - Livro Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Bloco+Q+-+Livro+Caixa
version: 18
---

Este bloco deverá estar preenchido para as pessoas jurídicas optantes pela sistemática do lucro presumido que se utilizem da prerrogativa prevista no parágrafo único do art. 45 da Lei nº 8.981, de 20 de janeiro 1995, e cuja receita bruta no ano seja superior a R$ 1.200.000,00 (um milhão e duzentos mil reais), ou proporcionalmente ao período a que se refere.

O Bloco Q é composto pelos Registros Abaixo:

0lefttrue001ConsistênciaAviso!

Antes de seguir com os passos, certifique-se de que o módulo Fiscal **possua** **integração** com o **Financeiro**.

01true1Passo 1

* No Cadastro de Filiais - Anexos | Parâmetros ECF - Escrituração Fiscal Contábil

Imagem2Passo 2

* Criar/Editar um registro
* Ir para pasta **Tributação**
* Selecionar o campo **Tipo Escrituração** como: "Não obrigada a entrega a ECD/Livro Caixa"
* Fazendo isso campo **Gerar Bloco Q - Livro Caixa** será habilitado

Imagem3Passo 3

* Após isso marque-o e salve a edição;
* Agora no Gerador de Saídas selecione no campo **Parâmetros ECF** o registro que habilitamos a geração do Bloco Q

ImagemQ001Q001REGISTRO Q001: ABERTURA DO BLOCO Q

**REGISTRO Q001: ABERTURA DO BLOCO Q**

Registro de controle gerado automaticamente pelo processo da ECF. Informa se existe ou não movimentação no bloco Q

| Nº | Campo | Descrição | Tamanho | Obrigatório |
| --- | --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo a identificação do registro (Q001). | 4 | Sim |
| 2 | IND\_DAD | Indicador de movimento: 0 – Bloco com dados informados. 1 – Bloco sem dados informados. | 1 | Sim |

Q100Q100REGISTRO Q100: DEMONSTRATIVO DO LIVRO CAIXA

**REGISTRO Q100: DEMONSTRATIVO DO LIVRO CAIXA**

Este registro passou a existir a partir do leiaute 2 da ECF, sendo de preenchimento facultativo para o ano-calendário 2015, e passando a ser exigido a partir do ano-calendário 2016), para as empresa tributadas pelo Lucro Presumido, quando 0010.TIP\_ESC\_PRE for igual a “L” (Livro Caixa).

| Nº | Campo | Descrição | Tamanho | Obrigatório |
| --- | --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo a identificação do registro (Q100). | 4 | Sim |
| 2 | DATA | Data da entrada ou da saída dos recursos. | 8 | Sim |
| 3 | NUM\_DOC | Número do documento. | - | Não |
| 4 | HIST | Histórico | - | Sim |
| 5 | VL\_ENTRADA | Valor de entrada dos recursos. | 19 | Não |
| 6 | VL\_SAIDA | Valor de saída dos recursos. | 19 | Não |
| 7 | SLD\_FIN | Saldo Final. | 19 | Sim |

Q990Q990REGISTRO Q990: ENCERRAMENTO DO BLOCO Q

**REGISTRO Q990: ENCERRAMENTO DO BLOCO Q**

Registro de controle gerado automaticamente pelo processo da ECF.

| Nº | Campo | Descrição | Tamanho | Obrigatório |
| --- | --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo a identificação do registro (Q990). | 4 | Sim |
| 2 | QTD\_LIN | Quantidade total de registros do Bloco Q. | - | Sim |
