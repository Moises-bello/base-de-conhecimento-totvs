---
content_hash: 029d87ff117a7d47e655e76d93f4960845a4043073ce99d897a170c6f58d09ce
fetched_at: '2026-06-29T00:11:36.023793+00:00'
page_id: '770945841'
product: rm
source: tdn-rm
title: FAQ - Erros - Criar Pessoas / Proposta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=770945841
version: 7
---

---

Para iniciar a utilização das propostas, é necessário realizar algumas validações no sistema, a fim de garantir que os dados estejam corretamente sincronizados para o uso do sistema integrado.

### Por coligada:

1. Validar no RM se o código do Cli/For está configurado como sequencial:   
   Acesse o cadastro de Cli/For no RM e verifique se o mesmo está parametrizado conforme o exemplo abaixo:
2. Validar se o usuário do Portal de imóveis encontra-se sincronizado com Cli/For (RM).  
   Para efetuar essa parametrização, é necessário acessar o menu de usuários no portal de Imóveis e verificar se os usuários existentes possuem registros correspondentes no Cadastro de Cli/For no RM. Caso não haja correspondência, é imprescindível realizar o cadastro dos usuários no RM, a fim de garantir a integração adequada entre os dois aplicativos. Essa sincronização de cadastros é fundamental para o correto funcionamento e alinhamento das informações nos sistemas envolvidos.
3. Validar a os registros do cadastro de pessoa do Portal de imóveis encontram-se sincronizados com Cli/For do RM.  

   Para validar essa parametrização, é necessário acessar o cadastro de Cli/For no RM e verificar se o registro da pessoa proveniente do cadastro de Pessoas do Portal está corretamente incluído.

   Em seguida, no Portal de Imóveis, ao editar essa pessoa, clique na opção "Sincronizar com o Backoffice" e, em seguida, salve as alterações. Essa ação garante a sincronização adequada das informações entre o portal e o sistema de gestão, assegurando a consistência dos dados.

### **Por empreendimento:**

---

1. Validar se a tabela de preços vinculada ao empreendimento encontra-se sincronizada com o RM.
2. Validar se a modalidade de venda parametrizada no RM encontra-se vinculada ao empreendimento.
3. Validar a modalidade de comissão do RM, está vinculada ao empreendimento.

Abaixo estão exemplos de como as mensagens de validação são apresentadas ao usuário caso os registros não estejam configurados corretamente, conforme as instruções de validação descritas anteriormente:

**Por coligada:**

1. Mensagem de validação: "Erro: Código Sequencial Parâmetro Cli/For não está configurado corretamente.."
2. Mensagem de validação: "Erro: Usuário PI não está sincronizado com Cli/For."
3. Mensagem de validação: "Erro: A Pessoa PI não está sincronizada com Cli/For."

**Por empreendimento:**

1. Mensagem de validação: "Erro: Tabela de Preço vinculada ao empreendimento não está configurada corretamente. Verifique as configurações e tente novamente."
2. Mensagem de validação: "Erro: Modalidade de Venda parametrizada e vinculada ao empreendimento não está configurada corretamente. Verifique as configurações e tente novamente."
3. Mensagem de validação: "Erro: Modalidade de Comissão vinculada ao empreendimento não está configurada corretamente. Verifique as configurações e tente novamente."

Essas mensagens são exibidas ao usuário para indicar que as configurações necessárias não estão corretas e orientá-lo a verificar e corrigir as configurações adequadas.
