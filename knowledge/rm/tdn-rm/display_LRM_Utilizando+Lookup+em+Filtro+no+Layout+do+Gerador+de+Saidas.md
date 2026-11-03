---
content_hash: 57087b7b919634428c3d7ce0bf8b2cd48dcd9d62af18704630fe644ba88bc94f
fetched_at: '2026-06-29T00:05:58.246660+00:00'
page_id: '185744627'
product: rm
source: tdn-rm
title: Utilizando Lookup em Filtro no Layout do Gerador de Saidas
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+Lookup+em+Filtro+no+Layout+do+Gerador+de+Saidas
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Gerador de Saídas                        **Versão:**11.80 |
| **Processo** | **:** | Utilizando Lookup em Filtro em Layout do Gerador de Saidas |
| **Subprocesso** | **:** | Informações da Página |
| **Data da publicação** | **:** | 17/03/2015 |

No exemplo abaixo será criado layout utilizando a tabela PFUNC onde teremos os campos "Coligada, Chapa, Nome e Salario" e será criado o Filtro utilizando o campo CHAPA.

1 - Crie um novo layout

2 – Adicione novo Arquivo e Registro

 

3 – Adicione novo Conjunto de Dados ao Contexto

 

4 – Com botão direito do mouse, clique em Propriedades para Adicionar tabela

 

5 – Clicando na reticencias, localize a tabela PFUN e adicione-a.

 

6 – Selecione os campos que serão utilizados (Coligada, Chapa, Nome e Salario) e adicione o Filtro utilizando como parâmetro o campo CHAPA.

 

7 – Adicione Parâmetro da Geração

 

8 – Adicione Lookup

 

9 – Adicione a Action a tabela PFUNC

 

10 – Configure os campos obrigatórios

 

11 – Na aba de configuração do Contexto 01, arraste o campo CHAPA do Contexto 02 para o parâmetro.

 

12 – Na aba de configurações do Registro 0001, adicione a tabela "Funcionários" do Contexto 01 arrastando-a para Ligação.

13 – Adicione os campos que serão configurados arrastando os campos para cada posição.

14- Configure os campos que são as chaves primarias na coluna "Modo".

15 – Salve o layout

 

Desta forma, ao gerar o layout você poderá digitar diretamente a CHAPA

 

Ou clicar na reticencias onde será apresent\_GoBackada tela de lookup para selecionar a CHAPA que deseja.
