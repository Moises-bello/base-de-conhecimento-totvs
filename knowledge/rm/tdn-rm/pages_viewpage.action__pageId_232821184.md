---
content_hash: b72891da4720d65d0a2ebfcf713b52fa0826a6dec6730436328feca60705a785
fetched_at: '2026-06-29T00:06:27.391596+00:00'
page_id: '232821184'
product: rm
source: tdn-rm
title: TUAUAY DT Integração com MS-CRM Versão 2011 ou Superiores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232821184
version: 125
---

# INTEGRAÇÃO COM MS-CRM VERSÃO 2011 OU SUPERIORES

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Business Conector |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Configura Integração | ConConfiguraIntegracaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Conceito | ConConceitoAction | |
| **Chamados Relacionados** | TUAUAY |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | Não há |
| **Sistema(s) Operacional(is):** | Windows |

## 

## Descrição

A integração entre a Linha RM com o Microsoft Dynamics CRM (MS CRM) proporciona a sincronização de cadastros e processos através do TOTVS Business Conector (TBC).

O objetivo desta implementação do TBC é possibilitar a integração da linha RM com as versões mais atuais do MS CRM (2011 ou superiores).

## Procedimento para Utilização

Para atualizar a sua integração utilizando o MS CRM na versão 2011 ou em alguma versão superior vá em *"Integração > Ferramentas > Configurar"* e clique em "Avançar".

Preencha a senha da base de dados RM, teste a conexão para validá-la e tendo sido a mesma validada com sucesso, clique em "Avançar".

Selecione a integração Linha RM x MS CRM e clique em "Avançar".

Na próxima tela preencha os campos:

* Diretório Conceitos: Informe o diretório onde se encontram os conceitos referentes a esta integração;
* Server URL: Informe a URL referente ao MS CRM;
* Domínio: Informe o domínio de rede;
* Usuário: Informe o usuário de rede;
* Senha: Informe a senha do usuário de rede;
* Versão MS-CRM: Informe se utilizará o MS CRM 2007 ou o MS CRM 2011 ou superiores;
* Testar Conexão: Antes de selecionar a Organização é necessário testar a conexão com o MS CRM para autenticar os dados de conexão;
* Organização: Informe a organização referente ao MS CRM.

Clique em "Avançar" e em seguida em "Concluir" para que o assistente realize as configurações necessárias.

**Assistente de Implantação de Processos**

Acesse: *"Integração > Ferramentas > Parâmetros"*e clique em "Avançar".

Selecione a integração *"Linha RM x MS CRM"* e clique em "Avançar".

Preencha os parâmetros informando o Usuário RM e a Senha RM que serão utilizados na comunicação entre a Linha RM e o MS CRM.

Clique em "Avançar", e após em "Concluir" para que o assistente realize as configurações necessárias.

**Alteração no Conceito de Produto**

Acesse *"Integração > Integração > Conceito (ETL)"*.

Selecione o conceito 'Cadastro\_Produto\_RM\_CRM' e abra a edição do mesmo.

Na aba *"Correspondências"* selecione a operação 'UOM' e em 'Alimentação' informe os valores correspondentes à organização do MS CRM instalada. Faça o mesmo para a operação 'UOMS'.

**Agendamento dos Conceitos**

Acesse *"Integração > Integração > Conceito".*

Selecione o conceito desejado e acesse *"Processos > Processar Conceito".*

**Importante**

 

Apenas os conceitos que tem como origem o banco de dados da Linha RM para o MS CRM devem ser agendados. Os demais conceitos não devem ser agendados, pois eles serão consumidos via MS CRM.

Os conceitos devem ser agendados na ordem citada abaixo pois há conceitos que necessitam de dados de outros conceitos (dependência):

1. Cadastro\_Aluno\_RM\_CRM;

2. Cadastro\_CliConta\_RM\_CRM;

3. Cadastro\_Contat\_RM\_CRM;

4. Cadastro\_Contrato\_RM\_CRM;

5. Cadastro\_Estado\_RM\_CRM;

6. Cadastro\_Modalidade\_RM\_CRM;

7. Cadastro\_Municipio\_RM\_CRM;

8. Cadastro\_Pagamento\_RM\_CRM;

9. Cadastro\_Produto\_RM\_CRM;

10. Cadastro\_Represent\_RM\_CRM;

11. Cadastro\_SitVenda\_RM\_CRM;

12. Cadastro\_TpParcela\_RM\_CRM;

13. Cadastro\_Transport\_RM\_CRM;

14. Cadastro\_Vendedor\_RM\_CRM;

15. Cadastro\_Empreend\_RM\_CRM.

O ideal é que os conceitos sejam agendados com um período de tempo entre eles, de no mínimo 30 minutos, devido à dependência de dados dos outros conceitos.

Além da configuração realizada na Linha RM também é necessário configurar o MS CRM (4.0 ou 2011).  Consulte essa configuração em [Como Fazer: Configuração do Microsoft Dynamics CRM 2011](http://tdn.totvs.com/pages/viewpage.action?pageId=45220765).

divs
