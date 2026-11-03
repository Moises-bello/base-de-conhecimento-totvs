---
article_id: 4413311208727
category: Funcionários
content_hash: ea58557dbdc4991bd4f240a811738b82aea537a42a94233487053e2ac3d7b244
fetched_at: '2026-06-28T22:47:03.376899+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Ativação da flag Membro CIPA no cadastro do funcionário
type: support-article
updated_at: '2026-05-22T19:36:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413311208727-RH-RM-FOP-Ativa%C3%A7%C3%A3o-da-flag-Membro-CIPA-no-cadastro-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:3:00 min** **Dúvida**Como habilitar a flag Membro CIPA no cadastro do funcionário?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9802284576535)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Esta opção só é disponibilizada na tela de cadastro do funcionário quando é utilizado o módulo Gestão de Pessoas. É necessário que os sistemas estejam integrados em **Ambiente | Parâmetros | Integrações de Sistemas**:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9802342368407)​​  
  
![](https://totvssuporte.zendesk.com/attachments/token/CB5HRTJtzZzjJMrsXKnZX7qcj/?name=inline-96314603.png)  
  
A parametrização da Cipa deve ser realizada diretamente no módulo **Gestão de Pessoas**. A flag **Membro CIPA** é marcada quando o funcionário é eleito pelo empregado ou pelo empregador como representante da Comissão criada. Já a estabilidade só será gerada quando o mesmo for eleito pelo empregado.   
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9803756508951)  
  
Neste caso só serão listados para serem inseridos como representantes os funcionários que são Candidatos na Eleição da CIPA.:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9803946918679)​  
  
Abaixo segue documentação relacionada ao cadastro da CIPA e todos os processos relacionados:  
  
[Comissões da CIPA](https://tdn.totvs.com/pages/releaseview.action?pageId=452719431)  
[Eleições](https://tdn.totvs.com/pages/releaseview.action?pageId=452719392)  
[Representantes](https://tdn.totvs.com/display/public/LRM/Representantes)  
  
Veja abaixo a relação dos Parâmetros referentes a CIPA:  
  
**Cargo Reservado para Funções da CIPA**  
Através do lookup será possível informar o cargo reservado para funções da CIPA. Somente as funções vinculadas a esse cargo serão visualizadas no cadastro de CIPA.  
  
**Usa convenção CIPA**  
Selecionando esta opção poderão ser definidos períodos superiores a 1 (um) ano para vigência da CIPA. Após selecionar esta opção, deverá ser informado no campo "Período de validade da CIPA (em anos)" qual será o período a ser considerado.  
  
**Período de Validade de CIPA (em anos)**  
Neste parâmetro serão informados os anos de validade da CIPA, o mesmo só será habilitado após a marcação do parâmetro: "Usa convenção CIPA".  
  
**Permitir Candidatos/Representantes com situação de afastamento**  
Marcando esse parâmetro será possível que empregados afastados participem das eleições da CIPA como candidatos.
