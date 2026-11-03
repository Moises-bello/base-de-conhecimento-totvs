---
content_hash: 53d696eae41718064b86368aba8266d73bb527a9c593082d24c8fa79a0369787
fetched_at: '2026-06-29T00:09:37.905848+00:00'
page_id: '425459648'
product: rm
source: tdn-rm
title: Linha RM x Microsoft Dynamics CRM - Configurações e Parâmetros da Linha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459648
version: 7
---

**Configurações e Parâmetros da Linha RM**

---

**Assistente de Configuração TOTVS Business Conector**   
    
 O TBC possui uma interface de configuração específica para cada pacote de integração. Para executar o Assistente de Configuração acesse: Integração | Ferramentas | Configurar.   
    
 Através do Assistente de Configuração serão importados para o TBC todos os Conceitos utilizados na integração, e também serão realizadas configurações de conexão com o MS CRM.  
    
 Os parâmetros necessários de configuração são:

* **Diretórios Conceitos:** Apontar onde estão localizados os Conceitos de uso exclusivo para esta integração.
* **Server URL:** Informar a URL referente ao MS CRM, sem os dados da organização. Exemplo: HTTP://RMinfra-crm2011:5555
* **Domínio:** Informar o domínio de rede.
* **Usuário:** Informar usuário de rede.
* **Senha:** Informar senha do usuário.
* **Versão MS CRM:** Informar qual a versão do MS CRM será utilizada (2007 ou 2011).

Após preencher estes parâmetros é necessário **Testar a Conexão**. Este recurso que autentica os dados de conexão, e deve ser realizado antes de preencher o parâmetro Organização.

* **Organização:** Informar a organização referente ao MS CRM

***Observação:*** A execução do Wizard de Configuração deve ocorrer sempre que alterações via atendimentos forem realizadas, pois durante correção é realizado manutenções no configurador.  
     
 **Assistente de Implantação de Processos do TOTVS Business Conector**  
    
 Além do configurador, o TBC também possui uma interface de parametrização específica para cada pacote de integração.  A parametrização da Integração da Linha RM x MS CRM é **obrigatória** e deve ocorrer depois da execução do Configurador.   
 Para executar o Assistente de Implantação de Processos acesse: Integração | Ferramentas | Parâmetros  
 Selecione a integração Linha RM x MS CRM e clique em avançar.   
    
 Os parâmetros necessários de configuração são:  
    
 • **Usuário RM:** Informe um Usuário referente à Base de Dados da Linha RM.   
 • **Senha RM:** Informe a senha do Usuário referente à Base de Dados da Linha RM.  
    
 Estes parâmetros serão utilizados para executar conceitos quando o sincronismo acontecer do MS CRM para a Linha RM.   
     
 **Alteração no Conceito**  
    
 Após realizar estas configurações, é necessário alterar o conceito referente ao cadastro de Produto. Acesse: Integração | Integração | Conceito.  
    
 Abra a edição do conceito "Cadastro\_Produto\_RM\_CRM".  
    
 Na aba Correspondências altere o valor das operações **"UOM"** e **"UOMS"** para os valores correspondentes a organização do MS CRM instalada.  
     
 **Agendamento dos Conceitos**  
    
 Os conceitos que tem como orgiem o banco de dados da Linha RM para o MS CRM devem ser agendados.  
 Acesse: Integração | Integração | Conceito.  
    
 Os conceitos devem ser agendados na ordem citada abaixo, pois há conceitos que necessitam de dados de outros conceitos (dependência).

1. Cadastro\_Aluno\_RM\_CRM.icp
2. Cadastro\_CliConta\_RM\_CRM.icp
3. Cadastro\_Contat\_RM\_CRM.icp
4. Cadastro\_Contrato\_RM\_CRM.icp
5. Cadastro\_Estado\_RM\_CRM.icp
6. Cadastro\_Modalidade\_RM\_CRM.icp
7. Cadastro\_Municipio\_RM\_CRM.icp
8. Cadastro\_Pagamento\_RM\_CRM.icp
9. Cadastro\_Produto\_RM\_CRM.icp
10. Cadastro\_Represent\_RM\_CRM.icp
11. Cadastro\_SitVenda\_RM\_CRM.icp
12. Cadastro\_TpParcela\_RM\_CRM.icp
13. Cadastro\_Transport\_RM\_CRM.icp
14. Cadastro\_Vendedor\_RM\_CRM.icp
15. Cadastro\_Empreend\_RM\_CRM.icp

Selecione o conceito e acesse: Processos | Processar Conceito.   
    
 ***Observação:*** Os demais conceitos **não devem** ser agendados, pois eles serão consumidos via MS CRM.

***Dica:*** O ideal é que os conceitos sejam agendados com um período de tempo entre eles, de no mínimo entre 30 e 30 minutos, devido a dependência de dados de outros conceitos.

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver mais detalhes da configuração:

[Configuração da Integração Linha RM x MS CRM](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-configuracao-e-parametros-da)
