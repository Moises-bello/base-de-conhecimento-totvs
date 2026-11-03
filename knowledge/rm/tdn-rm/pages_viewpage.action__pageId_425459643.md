---
content_hash: 8c70babcc67177af752842da8495ec01689f1e8ab0e55b0584e19648e290cb12
fetched_at: '2026-06-29T00:09:37.886381+00:00'
page_id: '425459643'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Cadastro de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459643
version: 4
---

**Backoffice RM x Protheus SigaMNT - Cadastro de Funcionário**

---

As inclusões, alterações de Funcionário são feitas através do módulo RH do sistema RM, que identifica o evento em sua entidade e envia uma mensagem única ao sistema Protheus SigaMNT. Através da sincronia de dados o Protheus recebe o cadastro do funcionário e pode utilizá-lo em seus processos de Manutenção de Ativos.   
   
A exclusão de um Funcionário ocorre através da execução de um processo, que caso não se comunique com o WebService do sistema Protheus ou falhe, exclui apenas do sistema RM o cadastro selecionado.   
   
**Pré-condições**  
   
1. Cadastro de todos os motivos, localizado em : RH/Folha de Pagamento/Administração Pessoal/Cadastros Globais/Tabelas Dinamicas. 2. Cadastro de Grau de Instrução. 3. Cadastro de Função. Localizado em:  RH/Folha de Pagamento/Administração Pessoal/Cargos – Funções/Função. 4. Cadastro de um Centro de custo com o mesmo código de um Centro de custo do Módulo Backoffice  em: RH/Folha de Pagamento/Administração Pessoal/Centros Custos. 5. Cadastro de Período  em: Executar/Ponto/Cadastro de período. 6. Executar o processo de Cadastro de período ativo/Definir Período Ativo. 7. Cadastro de Horários  em:  RH/Folha de Pagamento/Administração Pessoal/Horários. 8. Cadastrar uma Jornada nos Anexos do  menu Horários:  RH/Folha de Pagamento/Administração Pessoal/Horários/Anexos /Jornada. 9. Cadastro de Tipos de Funcionário. 10. Cadastro de Seção em:  RH/Folha de Pagamento/Administração Pessoal/Seção. 11. Cadastro de Sindicato em: RH/Folha de Pagamento/Administração Pessoal/Sindicato 12. No Protheus SigaMNT cadastrar: Função com Código: 00001. (Ver Informações Adicionais) 13. No Protheus SigaMNT cadastrar: Turno de Trabalho com Código  : 001 (Ver Informações Adicionais) 14. No Protheus SigaMNT cadastrar:Banco/Agência/Conta com códigos: 001/ 00000/0000000000.   
   
**Passos para a execução:**  
   
Passo  1 – Acessar o menu  :  RH/Folha de Pagamento/Administração Pessoal/Funcionário .

Passo  2 – Incluir um novo Funcionário.

Passo  3 – Preencher os campos de preenchimento  obrigatório, destacados em negrito  e  também os campos  que serão enviados ao Protheus e Salvar. Os campos enviados ao Protheus SigaMNT são:

**Aba Identificação :**

• Chapa

• Nome

• Dt.Nascimento

• Estado Natal

• Naturalidade

• Sexo

• E-mail

**Aba Documentação:**

• CPF   Aba Registro :  
• Data de Admissão

**Aba Salário/Jornada:**

• Tipo de Recebimento

• Salário Mensal

• Jornada

Aba Seção:

• Seção

**Observação:** O centro de custo do funcionário será obtido do campo Número do Centro de Custo, localizado na aba Dados Contábeis do cadastro de Seção.

Passo 4- Acessar o sistema Protheus , módulo SigaMNT.

Passo 5- Para visualizar os detalhes do cadastro enviado pelo sistema RM, selecione o Funcionário e clique em Visualizar:

Passo 6- Os campos exibidos na tela de cadastro de Funcionário no Protheus SigaMNT são:   
   
1. Aba Cadastrais

• Matricula

• Nome

• Data Nasc.

**2. Aba Funcionais**

• Centro Custo

• Data Admis.

• Dt. Demissao  
   
**3. Aba Nº. Documentos**

• CPF

4. Aba Outras Informações

• End. E-mail  
   
**Observações:**   
   
1. O centro de custo do funcionário será obtido do campo Número do Centro de Custo, localizado na aba Dados Contábeis do cadastro de Seção.  
   
2. Serão enviados ao Protheus SigaMNT somente os funcionários que possuierem o Tipo de Recebimento Mensalista ou Semanalista.  
   
3. A exclusão de funcionário é executada via processo, assim sendo, caso haja algum erro na integração a exclusão não será desfeita, sendo necessário seguir o seguinte processo:

* Selecione o funcionário e clique em Excluir Funcionário.
* Foi gerada uma mensagem de erro que impediu que a mensagem de exclusão fosse enviada ao Protheus SigaMNT.
* Analisar a mensagem de erro obtida
* Corrigir a origem do problema
* Reencaminhar a mensagem de integração

4.  Serão integrados somente funcionários cujo Tipo de Recebimento for igual à Mensalista ou Semanalista.

5.  O rateio de funcionário por centro de custos não será integrado, pois o mesmo não é utilizado pelo sistema SigaMNT.   
   
**Dica:** Caso o erro não seja sanado deve-se fazer a exclusão de forma manual

---

Para ver os detalhes do cadastro de Funcionário, acesse o boletim técnico.  
   
 **Recursos Adicionais**

TDN - Boletins Técnicos:

[Cadastrar Funcionário](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+FUNCION%c3%81RIO_BR_CON000158.pdf?version=1&modificationDate=1380044687000)

[Excluir Funcionário](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_EXCLUIR+FUNCION%c3%81RIO_BR_CON000158.pdf?version=1&modificationDate=1380044706000)
