---
article_id: 360005091392
category: Materiais - Compras (SIGACOM)
content_hash: 536f3fc9581f3c09d8bfe3c44fe2b1a2bedc0743bf5360cd7ee316a32a9872da
fetched_at: '2026-06-28T22:41:08.681819+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar operação
  triangular quando o encomendante não emite nota fiscal ao industrializador ?
type: support-article
updated_at: '2022-05-12T21:07:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005091392-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-opera%C3%A7%C3%A3o-triangular-quando-o-encomendante-n%C3%A3o-emite-nota-fiscal-ao-industrializador
---

**Dúvida**Como realizar operação triangular quando o encomendante não emite nota fiscal ao industrializador ?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

A nota fiscal do seu encomendante é obrigatória para que o Protheus realize o controle correto de poder de terceiros.

Para atender ao controle de poder de terceiro, atualmente é necessária a inclusão de uma terceira nota sem calculo de imposto (Não atualiza Livros Fiscal), não gera duplicatas, formulário próprio=não e somente atualiza estoque (poder de terceiros), na qual chamamos de Remessa Simbólica.

Definição do Processo (triangulação)

Nota 1 - Nota de Entrada (Emitida pelo Fornecedor) – Calcula Impostos, Gera duplicatas, Atualiza estoque e Gera Livro Fiscal.

Nota 2 - Nota de Saída (Remessa para o Industrializador) – Denominada Remessa Simbólica não calcula impostos, não gera duplicatas e não gera livro fiscal somente atualiza estoque e poder de terceiros.

Nota 3 - Nota de Entrada (Devolução do Produto Beneficiado pelo Industrializador) – Retorno de poder de terceiros calcula impostos, gera duplicatas, atualiza estoque e gera livro fiscal

Segue o descritivo com os métodos para atender o processo de triangulação de poder de terceiros para clientes que não concordam com a inclusão do movimento de cobertura simbólica (Nota 2).

Método 1 - O documento de cobertura (Nota Fiscal 2 – Cobertura) que esta sendo utilizado para controlar o saldo em poder de terceiros, pode ser configurado através da TES e de configurações de Serie/Espécie para não gerar livro, contábil, financeiro e NF-e. Neste caso esta inclusão será utilizada pelo sistema como uma movimentação somente para baixa de poder de terceiros.

Método 2 - Poderá ser utilizado o parâmetro MV\_ALMTERC para controlar saldo EM PODER de terceiros. Este parâmetro é utilizado para definir um armazém especifico para controlar todo o saldo em terceiros e neste caso o controle será efetuado pelos relatórios Kardex e pelo Registro de Inventario (MATR460).

Observações:

- Os métodos citados acima deverão ser validados por especialista da área junto ao cliente, tendo em vista que cada ramo de atividade possui características distintas, que podem alterar a metodologia aplicada resultando na aprovação ou não da metodologia junto a legislação.

- Os procedimentos acima foram avaliados pelo nosso departamento jurídico em Joinville/SC e qualquer duvida no processo peço que seja aberto um chamado direcionando o apoio para nossa equipe Jurídica, para que possamos avaliar qualquer divergência.

- Os exemplos acima podem sofrer variações de acordo com o processo utilizado em sua empresa.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
