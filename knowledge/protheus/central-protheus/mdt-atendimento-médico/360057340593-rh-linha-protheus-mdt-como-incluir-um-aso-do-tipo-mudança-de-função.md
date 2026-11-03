---
article_id: 360057340593
category: MDT - Atendimento Médico
content_hash: 4ca47a6fc7dd0c8b877c3fc31068fa6f710c5c312baad2fd0c1d23740922c0e2
fetched_at: '2026-06-28T22:44:20.662387+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como incluir um ASO do tipo Mudança de Função
type: support-article
updated_at: '2025-07-25T19:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057340593-RH-Linha-Protheus-MDT-Como-incluir-um-ASO-do-tipo-Mudan%C3%A7a-de-Fun%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27598212242839)**Tempo aproximado para leitura: 00:01:00 min **Dúvida**Como incluir um ASO (atestado de saúde ocupacional) do tipo Mudança de Função?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução** **1.** No modulo SIGAMDT acesse o menu no caminho: atualizações > atendimento medico > atestado ASO (**MDTA200**) e clique em incluir.  
  
É possível realizar a inclusão do atestado quando está fazendo a troca de função / tarefa / centro de custo ou departamento, para isso é necessário que o campo **Natureza** (TMY\_NATEXA) esteja selecionado com a opção **3=Mudança de Função**.  
  
A rotina possui os campos de  **Emp. Futura (**TMY\_EMPFUT) e **Fil. Futura** (TMY\_FILFUT), os quais são necessários caso o funcionário seja transferido para outra empresa ou outra filial, buscando as informações como risco e agentes do novo local de trabalho.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093816154)  
  
**2.** Botões

* **Riscos:** Para que o funcionário esteja exposto ao Risco, é necessário que as informações de função / tarefa / centro de custo / departamento, estejam dentro dos parâmetros definidos no Risco para onde o funcionário será transferido. É possível, através do parâmetro **MV\_NGMDTRI** selecionar os riscos que serão impressos no Atestado ASO, para isso, o conteúdo do parâmetro deverá estar como 2.
* **Agente:** Apresentará os agentes de riscos nos quais o funcionário esteja exposto, caso existam 2 riscos que possuam o mesmo agente, o sistema apresentará apenas um registro.
* **Exames:** Apresentará os exames do funcionário de acordo com o conteúdo do parâmetro **MV\_NGEXREL**, é necessário que o exame seja do tipo **Ocupacional**, que ele possua a mesma natureza que o ASO. Dentro da opção Exames, é possível relacionar exames que o funcionário tenha realizado através da opção Relac. Exames que possuam a natureza de exame diferente do ASO.  
    
  Exemplo botão exames:  
  Ao clicar em **+ Relac. Exames** é possível selecionar um exame relacionado, quando houver um exame realizado (com data de resultado).  
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096071293)  
    
  ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096071913)  
    
  ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096072173)  
    
  **Observação:**

Para exames que já contenham um aso vinculado, não será apresentado no momento da geração do novo ASO.  
  
O parâmetro **MV\_NGEXREL** possibilita relacionar os exames previstos (**sem data de resultado**) caso o mesmo esteja com o conteúdo igual a 2, caso contrário, apresentará apenas os exames realizados.

* **Questionário:** é possível realizar o vínculo do questionário que já tenha sido preenchido ou realizar a inclusão/alteração de um questionário. Através da opção Outras Ações \ Imprimir é possível realizar a impressão do questionário com as respostas.  
  ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096073673)  
    
  Impressão do Questionário:  
  ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093820454)
* **Restrições:** a opção é apresentada habilitada quando o campo **Ind. Parec. (**TMY\_INDPAR) está com o conteúdo igual a **3=Apto com Restrição**.   
  A restrição deve ser incluída se o funcionário possuir algum problema no momento de realizar uma certa tarefa no seu dia a dia. Caso o funcionário já tenha uma restrição vinculada através da rotina de **Ocorrências Ficha** (MDTA110), será apresentada na opção. É possível incluir, alterar ou excluir uma restrição.
* **Permissões:** as permissões devem ser incluídas e liberadas na rotina de **PT/PET** (MDTA992) e no momento da inclusão do ASO, poderão ser vinculadas.

**3.** Após cadastrar todas as informações necessárias clique em confirmar.  
E na tela onde é apresentado os colaboradores ao selecionar o ASO incluído, clique em Outras Ações \ Imprimir realizar a impressão do ASO.

Em caso de dúvidas na geração de exames consulte os artigos:

* [MP - MDT - Como relacionar exames em um Atestado de Saúde Ocupacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044751214-MP-MDT-Como-relacionar-exames-em-um-Atestado-de-Sa%C3%BAde-Ocupacional-?source=search)
* [MP - MDT - Como relacionar um ASO (atestado de saúde ocupacional) a um exame que não possui resultado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054827114-MP-MDT-Como-relacionar-um-ASO-atestado-de-sa%C3%BAde-ocupacional-a-um-exame-que-n%C3%A3o-possui-resultado?source=search)
* [MP - MDT - Quais as naturezas dos exames médicos ocupacionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054099313-MP-MDT-Quais-as-naturezas-dos-exames-m%C3%A9dicos-ocupacionais?source=search)
* [MP - MDT - Ao tentar relacionar um exame na rotina de ASO ocorre o aviso "Não foi encontrado nenhum exame para incluir nesse ASO". Ao incluir um aso demissional e clicar em exames para relacionar os exames."](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057340733)

**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[ASO Mudança de Função](https://tdn.totvs.com/x/bLoTEQ)
