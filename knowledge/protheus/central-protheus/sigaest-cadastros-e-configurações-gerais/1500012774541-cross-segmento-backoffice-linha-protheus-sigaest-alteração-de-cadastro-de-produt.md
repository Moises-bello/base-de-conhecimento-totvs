---
article_id: 1500012774541
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 7ade8ddcfe7015eb25565aad879a4fce26396cfe84238c92fa711dcf60ee02c5
fetched_at: '2026-06-28T22:39:08.016339+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Alteração de cadastro
  de produto via MILE - Erro fatal ao executar adapter. Como corrigir?
type: support-article
updated_at: '2026-05-13T16:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012774541-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Altera%C3%A7%C3%A3o-de-cadastro-de-produto-via-MILE-Erro-fatal-ao-executar-adapter-Como-corrigir
---

O erro "Erro fatal ao executar adapter" no processo Mile ocorre quando valores não podem ser atribuídos a campos específicos, como B1\_COD. Para corrigir, deve-se ajustar a expressão na Manutenção do Mile, usando, por exemplo, Pad(xa, Len(SB1-B1\_COD)). Caso persista, aplicar os pacotes acumulados do módulo Estoque/Custos e sempre realizar backup antes de atualizações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39770093995671) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Ao criar um processo Mile para determinada atividade, ocorre, no log o seguinte erro: "Erro fatal ao executar adapter." Como validar para corrigir esse problema?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

***Sugestão*****:**Assista abaixo o ***vídeo com exemplo prático sobre o processo alterar o Cadastro de Produtos pelo MILE*** no Protheus:

O mile é um processo muito pontual pois é configurável conforme a necessidade de cada usuário. Ele executa é uma Execauto, onde atribui os valores dos arquivos em uma execauto e cria os documentos.

Normalmente ocorrem-se erros como o que listaremos abaixo:

"Erro fatal ao executar adapter MATA010.  
| | SB1MASTER | B1\_COD  
FWNOUPDATE  
Valor não pode ser atribuido. (Codigo)  
B1\_COD ||

--

FWFORMMODEL:COMMITDATA(FWFORMMODEL.PRX)

"

Quando ocorrem erros apontando valores que não porem ser atribuídos, basta, no processo da Manutenção do Mile, delegar a expressão abaixo:

**Pad( xa , Len( SB1->B1\_COD ) )**

Perceba que neste exemplo acima, o valor que não estava podendo ser atribuído era B1\_COD da tabela SB1, por este motivo, a expressão está apontada para SB1 -> B1\_COD. É importante avaliar qual campo o seu processo Mile está apontando o valor não podendo ser atribuído para que faça a expressão corretamente.

Veja como ficaria na tela da Manutenção do Mile:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019714082)

**Caso persista ou esteja enfrentando um error.log**:

Se o error.log apontar em um processo Mile oriundo de rotinas do Estoque, basta aplicar o pacote acumulado do módulo:

**Pacotes acumulados Backoffice:**

[**- Acumulado BackOffice conforme sua versão**](https://tdn.totvs.com/x/2hgdHw)

Observação: Efetuar sempre o backup, antes de qualquer atualização, além de aplicar sempre primeiramente em ambiente de homologação.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
