---
content_hash: d54e03f3ac5bb86fb4f63e738ea7dee3aa9f8dec0a786f3fa45a9877cdb626f0
fetched_at: '2026-06-29T00:12:07.474010+00:00'
page_id: '926417025'
product: rm
source: tdn-rm
title: PI - Proposta - Condições de Pagamento - Segurança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=926417025
version: 3
---

---

**Objetivo:**  
Controle de Segurança da aba Condições de Pagamento  
  
**Pré-requisito para configuração de usuários no Portal de Imóveis**

---

1. **Verificar CPF do usuário CORRETOR no Portal de Imóveis (PI):**

   * Acesse o cadastro de usuários no Portal de Imóveis (USUARIO.CPFCNPJ).
   * Verifique se o CPF do usuário corretor corresponde ao CPF cadastrado em um registro de **Clientes/Fornecedores (FCFO.CGCCFO)** no RM.
2. **Criar usuário nos Serviços Globais do RM:**

   * Acesse os **Serviços Globais** no RM.
   * Crie um novo usuário utilizando o mesmo nome verificado no passo anterior.
   * Informe um perfil no Menu Acesso a Menus que possue as devidas permissões para este usuário corretor.
3. **Associar o usuário ao Cliente/Fornecedor no RM:**

   * Acesse novamente o cadastro de **Clientes/Fornecedores (FCFO)** no RM.
   * Localize e edite o registro que possui o mesmo CPF do usuário criado.
   * No **Menu Dados Adicionais**, informe o usuário de acesso criado nos Serviços Globais, esta associação irá permitir os acessos e permissões que serão vinculados para este registro de corretor.

Após seguir esses passos, o usuário estará devidamente configurado para acessar o Portal de Imóveis.

### **Informações da Tela:**

**Campo modalidade**: A opção só é carregada após os dados dos compradores serem informados no menu: Cliente e o ID da proposta ser exibido na tela. Isso significa que a proposta precisa estar em um estado válido antes da modalidade ser selecionada.

Quando o usuário seleciona uma modalidade de financiamento, o sistema verifica se a soma dos componentes da modalidade atinge exatamente 100% do valor da venda e carrega os componentes na visão da tela, os mesmos serão listados na visão podendo ser manipulados de acordo com a necessidade do usuário.

Esses componentes são predefinidos na modalidade cadastrada dentro do RM.

### **Controle de Permissões e Validações**

É possível limitar o acesso do usuário para edição dos componentes carregados na tela. Para isso, siga os passos abaixo:

1. **Acesse o RM** e localize o **Perfil** associado ao corretor.
2. No perfil, vá até a **Guia Acesso a Menus** e navegue pelo seguinte caminho:
   * **Venda** > **Contratos** > **Contratos de Venda - Parte 2** > **Contratos: Condições de Financiamento: Editar**.
3. **Retire o acesso desse menu** para impedir que o corretor edite os componentes da modalidade carregada na visão.

Ao realizar essa configuração, o corretor poderá visualizar os componentes, mas não conseguirá editá-los, conforme demonstrado na imagem abaixo.
