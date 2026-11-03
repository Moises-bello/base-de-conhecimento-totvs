---
content_hash: 38ecba5b69cc2698f0a1f660c9dc4446c7dfc0d62f0c7e13bf403d504888be36
fetched_at: '2026-06-29T00:10:08.505171+00:00'
page_id: '452719526'
product: rm
source: tdn-rm
title: Funções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719526
version: 10
---

### **Objetivo**

As funções representam as atividades desempenhadas na empresa e estão vinculadas aos cargos. Esse cadastro é essencial tanto para as rotinas da folha de pagamento quanto para a integração com o RM Vitae, solução de Gestão de Pessoas da linha RM.

**ATENÇÃO:**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em Cadastros | Segurança | Perfis | Acesso a Menus.  
Por meio desse cadastro, é possível controlar:

* + O que cada perfil de usuário pode visualizar ou acessar;
  + A liberação ou restrição de menus e funcionalidades no sistema.

### **Identificação**

Cargo

Todas as funções vinculadas a um determinado cargo podem ser visualizadas na janela de edição de Cargos, em Cadastros | Cargos.

Pontos

Campo livre que pode ser utilizado, por exemplo, por empresas que calculam eventos proporcionais com base na função.

**Observação:**

Os pontos podem ser usados para distribuir comissões entre os funcionários, de acordo com cada função. Essa informação pode ser utilizada em fórmulas para diversos fins. Deixe em branco caso não utilize esse recurso.

CBO

Código Brasileiro de Ocupação da função, utilizado em relatórios como CAGED e RAIS.

CBO 2002

Código atualizado conforme a **Portaria nº 397, de 09 de outubro de 2002**.

**Atenção:**

O campo CBO será mantido enquanto os relatórios CAGED e RAIS não forem atualizados para utilizar exclusivamente o CBO 2002.

Inativa

Funções marcadas como inativas não podem ser associadas a funcionários ativos. Além disso, funções já vinculadas a funcionários não podem ser inativadas.

Controle de Lotação

Estes campos ficarão desabilitados para os usuários que possuem o RM Vitae (Gestão de Pessoas) instalado, uma vez que, este sistema controla o limite de vagas em Opções | Parâmetros | RM Vitae | pasta Controle de Lotação.  
   
**Vagas**

Limite

Cadastre o número de vagas que são permitidas por função. Este campo controla o limite de funcionários dentro de uma função. Para as bases que não têm permissão ao RM Vitae e se o campo "Usa controle de Limite de Funcionários por Função" (Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros I) estiver marcado e o campo "Limite de Funcionários": Estiver com valor zero, o sistema irá apresentar, em casos de inclusão e transferência de funcionários, a mensagem "Limite de funcionários para esta função já foi esgotado". Estiver com um determinado valor, o sistema irá permitir a inclusão de um número de funcionários menor ou igual ao limite definido. Se o campo "Usa controle de Limite de Funcionários por Função" (Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros I) estiver desmarcado, o campo "Limite" será visualizado com o status de "Sem Controle" e o usuário poderá admitir quantos funcionários desejar.

Este campo permite cadastrar o número máximo de vagas permitidas por função, controlando assim o limite de funcionários que podem ser alocados em determinada função.

Para bases que não têm permissão ao RM Vitae, o comportamento do sistema dependerá da configuração do parâmetro: "**Usa controle de Limite de Funcionários por Função"**, existente no menu Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros I.

* + **Se o parâmetro estiver marcado:**

    - E o campo **"Limite de Funcionários"** estiver com valor zero, o sistema impedirá novas admissões ou transferências para essa função e exibirá a mensagem: **"Limite de funcionários para esta função já foi esgotado."**
    - E o campo **"Limite de Funcionários"** estiver com um valor maior que zero, o sistema permitirá a inclusão de funcionários desde que o total não ultrapasse o limite definido.
  + **Se o parâmetro estiver desmarcado:**

    - O campo **"Limite"** será exibido com o status **"Sem Controle"**, permitindo ao usuário incluir quantos funcionários desejar naquela função, sem restrições de quantidade.

Alocadas

Quantidade de funcionários que estão cadastrados nesta função.

Disponíveis

Exibe a quantidade de vagas ainda disponíveis para a função.

Este campo apresentará um valor diferente de 0 (zero) apenas nas seguintes situações:

* + Quando o parâmetro **"Usa controle de Limite de Funcionários por Função"** estiver marcado, através do menu Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros. ou
  + Quando a empresa estiver utilizando o **Controle de Lotação do RM Vitae,** através do menu Opções | Parâmetros | RM Vitae | Aba Controle de Lotação.

Em casos onde nenhum dos controles estiver ativo, o campo será exibido com valor zero, indicando que não há controle de vagas disponíveis para a função.

Excedentes

Este campo apresentará um valor diferente de 0 (zero) apenas nas seguintes condições:

* + Quando o parâmetro **"Permite incluir acima do limite na Função"** estiver ativado, através do menu Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros I*,* ou
  + Quando a empresa estiver utilizando o Controle de Lotação do RM Vitae, com o parâmetro **"Permite Admissões Acima do Limite"** também ativado, através do menu Opções | Parâmetros | RM Vitae | Aba Controle de Lotação*.*

Se nenhuma dessas opções estiver habilitada, o sistema não permitirá admissões além do limite, e o campo permanecerá com valor **zero**.

Pendentes

Potencial

**Verbas**

Os campos "Limite", "Alocadas", "Disponíveis" e "Excedentes" de Verbas não são para controle do RM Labore. Estes campos são informativos referentes aos clientes que possuem o RM Vitae e usam este controle interno disponível somente para o RM Vitae. Para os clientes que possuem o sistema RM Labore, no momento de inclusão de funcionários, estará validando de acordo com a parametrização do RM Vitae.

### **Descrição**

Informações relativas às atribuições (descrição de cada função). Se o cliente tiver permissão de uso ao RM Vitae (Gestão de Pessoas), uma vez digitada a informação no RM Labore, automaticamente o cadastro de funções (internas) do RM Vitae será atualizado e vice-versa.

### **eSocial**

Considerar como Função de Confiança/Cargo em Comissão

Essa flag tem o objetivo de destacar função gratificada, ou de confiança, nos moldes da legislação trabalhista, estatutária ou legislação própria do ente federativo.

**ATENÇÃO:** Ao marcar o flag, a função passará a ser enquadrada nos eventos S-1040.

Tipo de Atividade

### **Anexo - Funcionários que exercem a função**

Relação nominal dos colaboradores que atualmente desempenham a função em questão, incluindo matrícula, nome, cargo, e demais informações relevantes para identificação e análise.

### **Anexo - Seções que possuem a função**

Lista das seções/departamentos onde a função está alocada, indicando as áreas da empresa em que ela é exercida e, se aplicável, a quantidade de colaboradores por seção.

### **Anexo - Quadro de lotações**

Visão consolidada da distribuição dos colaboradores por local de trabalho, demonstrando a estrutura organizacional e a alocação da função em diferentes unidades, setores ou filiais.

### **Anexo - Grade de Remuneração**

Neste anexo é possível informar a Grade de Remuneração que contempla a Função vinculada à Posição de Hierarquia.

* **Descrição:** Identifica a remuneração.
* **Evento:** Identifica o evento da remuneração.
* **Exibe na posição:** Define se será exibida ou não na  Posição da Hierarquia.
* **Valor:** Define o valor de referência atribuído à remuneração.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Copiar Função entre Coligadas

[Diferenças entre as funções NDTRAB e NJTRAB](https://tdn.totvs.com.br/pages/viewpage.action?pageId=979009997)
