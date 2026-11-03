---
article_id: 360019906471
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: f9b43b9a5ab4e3aa2c2914fd3e3eb1cbf1c432d46951fc71f20896ca96b316f7
fetched_at: '2026-06-28T22:37:55.407483+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA151 - Instrução
  de Cobrança
type: support-article
updated_at: '2024-01-15T20:52:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019906471-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA151-Instru%C3%A7%C3%A3o-de-Cobran%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20596630960023)** Tempo aproximado para leitura:**00:05:00min  
  
Dúvida**Envio de instruções de cobrança bancaria.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA151 - Todas as versões  
  
**Solução**O sistema disponibiliza o envio de instruções via **CNAB** para os títulos que já estão em borderô e que foram enviados para o banco sem com isso gerar um novo borderô.  
  
Ao realizar uma alteração de vencimento e/ou valores em um título que já tenha sido enviado ao banco, o sistema permite ao confirmar essa alteração que seja vinculada a essa alteração uma ocorrência para ser utilizada posteriormente para gerar o arquivo de instrução de cobrança. O sistema permite vincular essa ocorrência tanto ao confirmar a alteração quanto clicar em Ações Relacionadas > Instr. Cobranças.

A gravação da instrução de cobranca, deve ser feita no momento do salvamento titulo, caso clique na opção "Não" e retorne a tela para salvamento, habilita a tela de instrução, mas não será gerado o registro na tabela FI2, visto que a última alteração foi cancelada, sendo necessário refazer o processo feito.  
  
Dessa forma, essas novas instruções ficarão registradas na tabela "**FI2**" e somente serão geradas no arquivo que será enviado enquanto estiverem pendentes de envio (**FI2\_GERADO = 2 - Não**) ou quando na rotina "Geração de Arquivo de Instruções" (**FINA151**) o parâmetro de configuração "Mostra já gerados?" Estiver configurado como "Sim".  
  
Procedimentos para gerar o arquivo de instrução de cobrança:  
No menu Comunicação Bancária > Instrução de Cobrança - preencha os parâmetros solicitados conforme orientação do help, com a devida atenção as seguintes perguntas:  
  
Arquivo Config. - informe o nome do arquivo de configuração. Este é o arquivo onde foram gravadas as configurações de parâmetros do **CNAB** no ambiente Configurador.  
Arquivo de Saída - informe o nome do arquivo de envio, seguindo a orientação do banco, ou criando um critério próprio.  
Confira os parâmetros e confirme.

No menu, selecione a opção "Gerar Arquivo" e se exibirão as ocorrências que serão enviadas. Selecione e confirme.  
Neste momento será gerado o arquivo cujos títulos tenham instruções cadastradas, conforme os parâmetros fornecidos.  
O arquivo estará disponível no diretório "\System\" ou em equivalente e para envia-lo, deve ser copiado ou então direcionar o aplicativo de transmissão a esse diretório.  
  
O código da instrução que deverá ser utilizado no arquivo de configuração é o campo "**Cód.Ocorrênc.**" (**E1\_OCORREN**) do Cadastro de Contas a Receber, atualizado a cada ocorrência cadastrada para o título na tabela "**FI2**".

**Saiba Mais**  
[How to | Instrução de Cobrança Receber - FINA151| #TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/watch?v=IHzKIW52ivY)
