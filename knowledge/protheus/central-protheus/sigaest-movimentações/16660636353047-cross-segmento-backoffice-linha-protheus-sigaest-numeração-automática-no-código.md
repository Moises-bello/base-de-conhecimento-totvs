---
article_id: 16660636353047
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 50b255a833dfccca386c1bb55a7d8eeaad319c2ba8847694f9dc971d1d91b1a6
fetched_at: '2026-06-28T22:38:57.229704+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Numeração automática
  no código do produto B1_COD
type: support-article
updated_at: '2026-06-19T18:24:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16660636353047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Numera%C3%A7%C3%A3o-autom%C3%A1tica-no-c%C3%B3digo-do-produto-B1-COD
---

O campo Código do Produto (B1\_COD) no Cadastro de Produtos (MATA010) do Protheus deve ser digitado manualmente, mas existe uma nova funcionalidade para gerar códigos automaticamente via categorização. É possível também customizar a numeração com a função GETSXENUM, porém essa prática pode causar falhas e lentidão. Recomenda-se que personalizações sejam feitas por especialistas para evitar problemas.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16660613066263) Tempo aproximado para leitura 00:06:00 min**  
  
**Ocorrência**  
Como configurar o campo de Código do Produto (B1\_COD), no Cadastro de Produtos (MATA010), para trazer a numeração automaticamente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
A rotina de Cadastro de Produtos (MATA010) foi desenvolvida de forma que o campo Código do Produto (B1\_COD) deve ser digitado manualmente.

No momento da gravação do registro há uma validação que verifica a existência de outro cadastro com o mesmo códugo na mesma filial, caso identifique, exibindo então o help "Código" ao usuário e solicita a troca do código, de modo a evitar duplicidade.

**É possível implementar um controle de numeração padrão no cadastro do produto?**

O time de Vendas desenvolveu uma funcionalidade vinculada ao cadastro de Categorização e caracterização de produtos, que padroniza gerando automaticamente o código dos produtos.

Para saber mais sobre este processo, acesse a documentação do link:

* [**Categorização e caracterização de produtos - Códigos de Produtos**](https://tdn.totvs.com/x/N1LePQ)

**É possível customizar o campo para carregar uma numeração automática?**

Há clientes que optam por personalizar o controle de numeração de forma simplista, diretamente no Dicionário de Dados (X3\_RELACAO), utilizando-se da função como "EXEMPLO" > [**GETSXENUM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810731-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-a-fun%C3%A7%C3%A3o-GetSXENum) no Inicializador padrão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19479482646679)

Porém, essa função pode ocasionar falhas, uma vez que não trata saltos de numeração, podendo gerar também:

* Lentidão/Travamento na inclusão do cadastro;
* Perda de referência do código sequencial utilizado (gerando a necessidade de efetuar manutenções no controle de numeração);
* Problemas de sequencial já gravados;
* Gerar reservas simultâneas de numeração, gerando saltos/perdas de numeração.

|  |
| --- |
| **Havendo a necessidade de automatizar o controle de numeração sequencial de forma customizada, é muito importante que a personalização seja elaborada por um especialista, evitando estas, dentre outras falhas não mapeadas.**  **Para assuntos sobre customizações TOTVS, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de pontos de entrada e rotinas automáticas documentadas  no portal TDN para uso no produto padrão.** **Estas documentações possuem exemplos de utilização previamente testados, caso utilize estes e o resultado seja diferente do documentado ou apresente falha, caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time Hub Plataformas (**[**hub.plataformas@totvs.com.br**](mailto:hub.plataformas@totvs.com.br)**).**  **Esta equipe oferece os serviços de criação e manutenção de fontes Protheus, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).** |

**Como corrigir a numeração automática de uma tabela?**

Veja um vídeo explicando o conceito de controle de numeração e como corrigir inconsistências:

**Importante:** Caso seja implementado um controle de numeração personalizado no campo, o time de Suporte padrão não realiza manutenções ou ajustes.

**É necessário acionar um consultor Protheus programador para mapear os impactos, conforme sua regra de uso, e personalizar o controle de numeração atendendo à todos os critérios e boas práticas.**

Conheça também a plataforma colaborativa [**DEVFORUM**](https://devforum.totvs.com.br/) da TOTVS para trocar recomendações entre programadores Protheus.

**Saiba mais:**

[Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](http://tdn.totvs.com/pages/releaseview.action?pageId=235570751)

[***Como realizar o ajuste no controle de numeração***](https://youtu.be/BhEo-9FFUIQ?si=hFMX9f6ACiSOWFKF)  
[***Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque***](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
