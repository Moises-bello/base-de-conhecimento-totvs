---
article_id: 20061858184343
category: SIGAEST - LEGAIS
content_hash: 9e817b978c686ca8483530b3ae7356fc2f9453dac50529c3b373b6c11dac03ce
fetched_at: '2026-06-28T22:38:51.628815+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar a Operação
  Triangular no papel de Industrializador sem a nota de cobertura ?
type: support-article
updated_at: '2023-12-22T18:11:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20061858184343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-a-Opera%C3%A7%C3%A3o-Triangular-no-papel-de-Industrializador-sem-a-nota-de-cobertura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20061858169623) Tempo aproximado para leitura: **00:04:23min****Dúvida**Por questões legais de alguns estados a Nota de Cobertura não é obrigatória, nesses caso, como realizar a operação triangular no papel de industrializador ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Como sabemos dentro do Protheus para que possamos realizar o controle do Poder de Terceiros, temos que alimentar a tabela SB6 (tabela de controle de poder de terceiros), e dentro do processo de operação triangular o passo que grava as informações nessa tabela seria exatamente no documento de cobertura, para que o Protheus consiga atender esses clientes que estão desobrigados a realizar a nota de cobertura, porém manter a amarração do processo de operação triangular com o controle da SB6 se faz necessário a criação de alguns campos:

**Passo 1:**

Criação dos campos:

SF1 | F1\_CLIPROP | tipo caracter | tamanho 6 | formato @! | titulo Cli.Propr | descrição Cliente proprietario | consulta padrão SA1     
   
SB6 | B6\_CLIPROP | tipo caracter | tamanho 6 | formato @! | titulo Cli.Propr | descrição Cliente proprietario |  consulta padrão SA1     
   
SF1 | F1\_LJCLIPR | tipo caracter | tamanho 2 | formato @! | titulo Lj Cli.Pro | descrição Loja Cliente proprietario      
   
SB6 | B6\_LJCLIPR | tipo caracter | tamanho 2 | formato @! | titulo Lj Cli.Pro | descrição Loja Cliente proprietario

Para maiores detalhes sobre a criação dos campos acima, [cliquei aqui](https://tdn.totvs.com/display/public/PROT/Entrada+de+beneficiamento+sem+documento+de+cobertura+MATA103+-+Estoque+-+P12).

**Passo 2:**

No momento de receber o material que foi enviado pelo fornecedor, deve selecionar o tipo da nota como Beneficiamento e esse fornecedor, deve estar cadastrado como Cliente em seu ambiente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20061893820055)

**Passo 3:**

Utilizar uma TES que realize o controle de poder de terceiros (F4\_PODER3 = R) e que atualize o estoque (F4\_ESTOQUE = S);

**Passo 4:**

Na Aba "Informações Adicionais" será informado o cliente proprietário (O Encomendante)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20062084828823)

Em resumo com essas configurações, será realizada uma entrada de nota, atualizando o seu estoque, e informando o seu fornecedor envolvido na operação triangular, nessa mesma nota é informado a TES controlando poder de terceiros e apontando o Encomendante (Cliente proprietário)

**Importante:** Na MATA410 (Pedido de Venda) clicar em F12 e deixar a opção Op. Triangular = Sim:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20062108052119)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
