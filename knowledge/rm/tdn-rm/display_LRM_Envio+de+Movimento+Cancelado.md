---
content_hash: fe983c68f09446eaa6aaf0e7ede0869a88e2ea48b49b8d093a94ec3ad5185403
fetched_at: '2026-06-29T00:10:53.766264+00:00'
page_id: '585309680'
product: rm
source: tdn-rm
title: Envio de Movimento Cancelado
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+Movimento+Cancelado
version: 3
---

Conforme as regras de cada prefeitura pode ser necessário informar o código do motivo de cancelamento do documento. Neste caso deve ser criado o campo complementar abaixo no movimento e parametrizados no tipo de movimento.

### **Passo a passo:**

1. Acesse *BackOffice|Gestão de Estoque, Compras e Faturamento* e clique na aba "*Cadastros*"

2. Ao lado direito do menu *"Tabelas de Classificação"*, clique no menu *Mais...|Campos Complementares|Movimentos*

3. Adicione o novo campo complementar *"CODMOTCANC":*

| Nome da Coluna | Descrição | Tipo | SubTipo | Tamanho |
| --- | --- | --- | --- | --- |
| CODMOTCANC | Código do motivo do cancelamento do documento | Alfanumerico | Texto | 2 |

4. Clique na aba *"Ambiente"* e menu *Parâmetros|Gestão de estoque, compras e faturamento*

5. Selecione seu *Tipo de Movimento*

6. Selecione o parâmetro *"Mov - Campos Complementares"* vincule o campo complementar criado no **Passo 3** ao movimento  
e finalize o processo.

7. Acesse um Movimento e informe o valor 1, 2 ou 3 para o campo complementar criado e salve  
(1. Extravio | 2. Dados incorretos | 3. Substituição )

Informações Adicionais

Mapeamento de campos: <https://tdn.totvs.com/x/1ONqIQ>
