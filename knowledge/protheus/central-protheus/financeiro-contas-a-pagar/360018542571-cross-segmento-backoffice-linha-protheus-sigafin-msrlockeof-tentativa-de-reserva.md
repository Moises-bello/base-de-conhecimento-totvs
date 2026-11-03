---
article_id: 360018542571
category: Financeiro - Contas a Pagar
content_hash: 66b5f3536d64072836df4cd517d8056384198cf1b9528c8044332c7656e1d926
fetched_at: '2026-06-28T22:38:08.413553+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento BackOffice Linha Protheus - SIGAFIN - MSRLOCK.eof Tentativa
  de Reservar o registro Alias SE5 em EOF
type: support-article
updated_at: '2026-01-05T20:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018542571-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-MSRLOCK-eof-Tentativa-de-Reservar-o-registro-Alias-SE5-em-EOF
---

**Ocorrência**

Tentativa de reservar registro no Alias em EOF Stack de chamadas em MSROCK.eof .Tenta novamente? Essa mensagem será fechada em 5 segundos.  
  
**Ambiente**

Protheus – Financeiro – A partir da versão 12.1.17

**Causa**

A mensagem “EOF Stack em MSRLOCK” não indica que o registro esteja bloqueado por outro usuário ou processo.

EOF significa End Of File (Fim de Arquivo).  
Ou seja, a rotina tentou reservar (lock) um registro para processamento, porém o ponteiro da tabela estava em EOF, indicando que o registro esperado não foi localizado.

Em termos práticos, o erro ocorre quando o sistema tenta manipular um registro que não existe, está inválido ou possui quebra de integridade referencial.

**Possíveis Causas**

O erro ocorre quando:

A rotina executa um DbSeek() ou lógica equivalente;

O registro não é encontrado na tabela;

Mesmo assim, o sistema tenta realizar um lock (MSRLOCK) sobre esse registro inexistente;

Como o ponteiro está em EOF, o Protheus gera a mensagem e grava o log msrlock.eof.

Portanto, não se trata de concorrência de usuários, mas sim de dados inconsistentes ou inválidos.

Exemplos comuns de causa

Se o erro ocorre, por exemplo, ao gerar ou excluir um Documento de Saída, pode existir inconsistência em algum dado relacionado, como:

TES inválido ou inexistente

Cliente / Fornecedor / Loja com código inexistente

Produto inválido no grid

Condição de pagamento inexistente

Item, natureza, conta, ou outro código referenciado que não exista na tabela correspondente

Ou seja, algum relacionamento necessário para o processamento não foi localizado, causando a tentativa de lock em EOF.

<http://tdn.totvs.com/pages/releaseview.action?pageId=235575485>

<http://tdn.totvs.com/pages/releaseview.action?pageId=6814812>
