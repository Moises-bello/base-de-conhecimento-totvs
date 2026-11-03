---
content_hash: cad672eac4aedbc65957f19e2853140736797d2a5c46b130e1e04d049667b2d3
fetched_at: '2026-06-29T00:11:13.502262+00:00'
page_id: '66126694'
product: rm
source: tdn-rm
title: Fórmulas em VB.NET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126694
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.50 |
| **Processo** | **:** | Fórmulas |
| **Subprocesso** | **:** | Fórmulas em VB.NET |
| **Data da publicação** | **:** | 09/07/2013 |

Objetivo:  Esta funcionalidade tem como objetivo permitir que usuários também utilizem da linguagem VB.net para elaborar e executar fórmulas no RM.exe, além das Fórmulas RM.

**Exemplo 1**

1. Acesse: Serviços Globais | Administração | Cadastros | Fórmulas.
2. Após definir e executar um filtro para o cadastro de fórmulas, selecione um Sistema. Neste caso usaremos o sistema RH | Folha de Pagamento.
3. Logo após, clique no botão Incluir, para que o a janela de inserção de uma nova Fórmula seja exibida. Preencha os campos Código e Título. No campo Linguagem, selecione a opção **VB. NET**.
4. Escolha a função desejada, entre as disponíveis. Neste caso usaremos a função Folha.DataNascimento.
5. Clique duas vezes com o mouse para que a função seja inserida.   
   Obs: para usar fórmulas VB.Net a sintaxe requer o uso da palavra reservada RETURN e em seguida a função desejada.   
     
   **RETURN Folha.DataNascimento**
6. Clique em Salvar. Será exibido o contexto do módulo de Folha de Pagamento.
7. Clique em Ok. De acordo com o contexto aplicado, o resultado será exibido.
8. Para mudar o contexto, basta clicar em "Contexto" .
9. Contexto aplicado, clique em "Resultado"   e o novo resultado é exibido.
10. Após,  clicar no botão "Salvar", o sistema irá registrar a fórmula em VB.NET, exibindo a mesma na listagem de fórmulas do sistema.

---

**Exemplo 2**

1. Neste segundo exemplo será utilizado outro módulo dentro do cadastro de fórmulas: BackOffice | Gestão de Estoque, Compras e Faturamento.
2. Será utilizada a função que retorna a data de emissão do movimento RETURN **Movimento.DataEmissao** .
3. Salve e será exibido o contexto correspondente.
4. Resultado exibido conforme contexto.

---

**Exemplo 3**

1. Outro exemplo simples com a utilização de variáveis. Escreva: **Dim** <nomeDaVariável> **as** <tipoDaVariável>.
2. Faça as operações necessárias.
3. Use a palavra return para exibir o resultado.

                                           

---

**Exemplo 4**

1. Utilize uma função global.
2. **RETURN** Globais.AnoDaData("**09/07/2013**")

Atenção

* Sempre que for usar uma fórmula VB.NET atente-se para o fato da sintaxe requerer o uso de RETURN para exibição do resultado. Caso contrário, será exibido "0" (zero) não devido ao erro do sistema, mas pela falta dessa palavra reservada.
* Para mais informações sobre a linguagem VB.NET consulte no site da [Microsoft](http://msdn.microsoft.com/pt-br/library/cc580664.aspx).
Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br:11500/WikiHelp/GLB/GLB.Formulas.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
