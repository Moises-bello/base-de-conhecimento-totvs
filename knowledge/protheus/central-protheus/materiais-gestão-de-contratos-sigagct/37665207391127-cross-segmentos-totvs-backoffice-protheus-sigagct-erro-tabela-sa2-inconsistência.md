---
article_id: 37665207391127
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 655bdcc7b36e161ab5fefedb1fe2f305c2cb0f3f046fa6e075d721d619d0b73f
fetched_at: '2026-06-28T22:37:24.233598+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos – TOTVS Backoffice Protheus - SIGAGCT - Erro "Tabela SA2 -
  Inconsistência nos Itens" ao encerrar uma Medição de Contrato
type: support-article
updated_at: '2026-04-07T16:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37665207391127-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGAGCT-Erro-Tabela-SA2-Inconsist%C3%AAncia-nos-Itens-ao-encerrar-uma-Medi%C3%A7%C3%A3o-de-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37665207383959) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao encerrar uma medição de contratos ocorre o erro "Inconsistência nos Itens" mencionando a tabela SA2

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37665223901079)

Para medições automáticas feitas pelas CNTA260 pode-se ocorrer a mensagem conforme exemplo abaixo no log de execução da medição automática:

--------------------------------------------------------------------------------  
Tabela SA2 02/04/26 09:02:34  
Inconsistencia nos Itens  
--------------------------------------------------------------------------------  
Medicao/entrega gerada com sucesso - 002960  
Contrato - 000000000000113  
Filial - 0101  
Competencia - 04/2026  
Erro no encerramento da medicao/entrega - Contrato - 000000000000113  
Planilha - 000002  
Competencia - 04/2026  
Filial - 0101

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Uma possibilidade da ocorrência de mensagem de inconsistência em tabela de cadastro, possa ser que por algum motivo no contrato do ambiente em questão por algum ele não esteja identificando o cadastro vinculado a ele no momento do encerramento pra se gerar o pedido de compras.

Uma analise da base que pode ser realizada, é fazer um cadastro de um novo contrato com as mesmas informações deste que ocorre a questão e verificando se ocorre alguma mensagem.

Onde caso não ocorra a mensagem, possa ser analisado os registros do cadastro do contrato que esta ocorrendo com os registros deste novo contrato que não ocorreu a mensagem, verificando alguma possível diferença e assim realizar o ajuste.

No cadastro do contrato as informações do fornecedor ficam nas tabelas CNC, CNA. e posteriormente levado pra inclusão da medição na tabela CXN.

Outra analise do ambiente, que pode-se também avaliar na base de dados são as configurações do campos de código e loja de fornecedor dessas tabelas do contrato (CNC, CNA), medição (CXN) e também da tabela do pedido de compras SC7. se se encontram com o mesmo tamanho e configurações.

Se verificando ainda assim persista ou não identifique:

1. Realize a atualização em ambiente de Homologação com os pacotes de correção adequados:
   * [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)
   * [Acumulado Gestão de Contratos conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)

     Obs: Após cada atualização, aplique os arquivos de dicionário e rode o comando `upddistr`.
   * Pacote [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)
2. Execute os testes desativando as customizações do ambiente utilizando os três métodos especificados na documentação.

   [Cross Segmentos - Linha Protheus - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)
3. Caso nos testes ainda ainda assim apresentem o mesmo comportamento, orienta-se a abertura de ticket no suporte para a analise enviando:

   * Envie um vídeo demonstrando todo o processo, desde o cadastro de um novo contrato, incluindo as condições e particularidades relevantes.
   * Informe o comportamento inconsistente encontrado, demonstrando cadastrais como:
     + Tipos de Contrato (CNTA021)
     + Tipos de Planilha (CNTA230)
     + Tipos de Revisão (CNTA010) caso a inconsistência ocorra no momento da revisão.
   * No vídeo, mostre os dados do Cabeçalho do Contrato, Planilhas, Itens das Planilhas, Cronograma financeiro, físico e contábil, se aplicável.
4. Encaminhe um arquivo `.csv` atualizado com as datas das fontes.

***Saiba Mais :***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
