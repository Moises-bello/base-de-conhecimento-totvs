---
content_hash: 4077f2db18cbdf643e5a958b7588d15c8fac84d4960f730b7fec2903055d5fa3
fetched_at: '2026-06-29T00:11:20.654405+00:00'
page_id: '687164552'
product: rm
source: tdn-rm
title: Padrão WinForms
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687164552
version: 8
---

# **[Portabilidade e Arquitetura](https://tdn.totvs.com/display/public/LRM/Portabilidade)**

# 

# **Diagrama visual da arquitetura IMB**

1. .

# **1)** **Nomenclatura****de Dlls**

---

Ao criar Dlls no módulo Common do TCGI

* **Form**: RM.Imb.Nome.Form;
* **Intf:**RM.Imb.Nome.Intf;
* **Data**: RM.Imb.Nome.Data;
* **ISever**: RM.Imb.Nome.IServer
* **Sever**: RM.Imb.Nome.Server

Ao criar Dlls no módulo de Vendas

* **Form**: RM.Imb.Venda.Nome.Form;
* **Intf:**RM.Imb.Venda.Nome.Intf;
* **Data**: RM.Imb.Venda.Nome.Data;
* **ISever**: RM.Imb.Venda.Nome.IServer
* **Sever**: RM.Imb.Venda.Nome.Server

Ao criar Dlls no módulo de Aluguel

* **Form**: RM.Imb.Aluguel.Nome.Form;
* **Intf:**RM.Imb.Aluguel.Nome.Intf;
* **Data**: RM.Imb.Aluguel.Nome.Data;
* **ISever**: RM.Imb.Aluguel.Nome.IServer
* **Sever**: RM.Imb.Aluguel.Nome.Server

# **2) Heranças**

---

# Ao criar um cadastro

Seguir o padrão de tela:

 Simples: ***ImbCobrancaAcaoAction***

 Complexa: ***ImbVendaContratoAction***

#fffAction

Utilizar a Herança***ImbActionMasterView***

#fffForm

Utilizar a Herança ***ImbFormEdit*** ou ***ImbFormEditNavBar***

#fffIntf

No caso de vendas, sempre cadastrar Resources  do Props no projeto ***"RM.Imb.Venda.Resources"*** para reutilizar os nomes.

Sempre utilizar a Herança ***DataSetProperties***

#fffData

Utilizar a Herança ***ImbDataServer***

Utilizar a sempre as tags  ***RMSSecurityFilterAttribute , RMSServerInfo*** e ***RMSServerSecurityInfo***

***Importante:** versão 12.1.29 e superiores, RMSSecurityFilterAttribute passou a ser obsoleto, agora utilize **[RMSSecurityFilter(CodSistema.Imb, 813000316, 0)]**o numero da tag de segurança é o padrão da liberação de consumo do server.   
**Atenção:**Override o método DoReadRecordSecurityFilter, para que não ocorrá erro, informando que não pode consumir readrecord de dataserver ao ser consumido via WSDataServer (PDC, PI e terceiros poderam chamar metodos publicos que consomem 'ReadRecord' no server).   
Exemplo de override:  
  protected override void DoReadRecordSecurityFilter(DataSet dataSet, object[] primaryKey, object ownerData)  
    {  
      DoReadRecord(dataSet, primaryKey, ownerData); // Caso não tenha nenhuma restrição de acesso por usuário a row, se tiver tem que implementar a regra.  
    }*

#fffIServer

Utilizar a Herança ***IRMSModule***

#fffServer

Utilizar a Herança***RMSModule***

# Ao criar um Processo

Seguir o padrão de tela:

 Simples: ***ImbGerarAcaoCobrancaManualAction***

 Complexa: ***ImbGerarAcaoCobrancaManualAcaoAction***

#fffAction

Utilizar a Herança***ImbActionProc***

#fffForm

Utilizar a Herança***ImbFormParamsProc***

#fffIntf

Utilizar a Herança ***ImbParamsProc***

#fffData

Utilizar a Herança***ImbMaquinaCalculoProcess ou ImbProcess***

Utilizar a sempre as tags  ***RMSServerInfo*** e ***RMSServerSecurityInfo***

***Importante:** A Tag 813000329 é relacionada a segurança do processo, atenção para não criar nova tag, quando o processo for apenas um facilitador para criação de vinculos para cadastros que já possuem a tag de segurança, nestes casos, quando já se tem permissão para cadastrar um objeto, o vínculo dos demais segue a mesma tag.*

# **3) Check-List**

---

1. Documente o seu código;
2. Não deixar método vazio e nem código fonte comentado;
3. Utilizar **Resources** em todas as mensagens para o usuário;
4. Não instanciar classes de server no cliente e vice-versa;
5. Evitar loops no cliente;
6. Sempre crie o objeto remoto utilizando blocos using();
7. Diminuir o IO com o banco de dados
   1. Ler todos os dados de uma só vez (eliminando acesso ao banco dentro de loops);
   2. Não utilizar valores constantes nas sentenças SQL e evitar a criação de sentenças SQL criadas dinamicamente;
   3. Não esquecer de colocar (NOLOCK) nas sentenças;
   4. Ao escrever uma cláusula WHERE, sempre colocar a cláusula mais restritiva antes;
   5. No SELECT, trazer apenas as colunas necessárias;
8. Ao final do processo executar o Check-dll, executar a seguinte  em  e executar o processo em C:\CorporeRM\RMCheckDll;
9. Analisar o sonar parar não criar novas pendencias;
10. Procure criar testes unitários em processos e cadastros com regra de negócio;
11. Revisar documentação a garantir que não existem informações de clientes indevidamente;
12. Realizar o Code Review do código fonte;
