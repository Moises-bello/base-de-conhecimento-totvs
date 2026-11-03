---
article_id: 19820864954263
category: Materiais - Compras (SIGACOM)
content_hash: 6b0cacde35692a9cfa8ac2cb665cf803672120b1b34d45cf1193d381f1150035
fetched_at: '2026-06-28T22:41:13.126239+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alias does not exist
  SX2 ( PREVIOUS ERROR : Alias does not exist SC7 )  on CHKFILE(APLIB200.PRW)'
type: support-article
updated_at: '2025-06-29T02:09:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19820864954263-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Alias-does-not-exist-SX2-PREVIOUS-ERROR-Alias-does-not-exist-SC7-on-CHKFILE-APLIB200-PRW
---

* ![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19820850646167) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao acessar uma rotina no sistema, sistema gera errorlog abaixo:

  ***Alias does not exist SX2***  
  ***( PREVIOUS ERROR : Alias does not exist SC7 )***  
  ***on CHKFILE(APLIB200.PRW)***

  *\*Esse errorlog pode ser gerado com diversas rotinas e suas respectivas tabelas. Trata-se de um caso genérico.*

  **Ambiente**Protheus – Compras – A partir da versão 12.1.33  
    
  **Causa**Geralmente o error.log ***Alias does not exist SX2*** *ocorre quando algum processo tenta utilizar alguma tabela do sistema porém naquele momento o dicionário de dados está inapto (fechado) para uso. Falando pontualmente do error.log quando acessamos o menu as funções de menudef são automaticamente executada, até mesmo os pontos de entradas. Em alguns cenários, esses pontos de entrada tentam abrir algumas tabelas ocasionando o erro, uma vez que n*o menudef das rotinas, só pode ser consultada a tabela SX6, pois todas as outras tabelas (SX2, SX3, tabelas de negócio) não estão abertas nesse momento quando a chamada do menu é feita por fora.   
    
  Esta tratativa também visa melhorar o tempo de carregamento dos menus de forma geral, pois sem acessar tabelas no carregamento do menu, o tempo do mesmo será mais rápido.  
    
  Esse comportamento é previsto na documentação sobre o menudef: <https://tdn.totvs.com/display/public/framework/MenuDef>

  ![image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWWiC7hqn6GR%2BkUfhIbLCW0OPSxW1yEVi8cAR8bBjageZqSh7i5zLlqsJhVKj5OwvUV3Ask1Lr%2FaYWulSsK2581gtMUChTL9BX%2BqcavlyisPxgkP%2FwaIrdeMwPLp7bTuLXf%2B21j6AvkPVw6n6ed8885k3hC0QLqgCU0s4Flx2IKRE9vB9xyMx65hYW%2FlU6HRCaJenAhdguSQ96F%2FIDC6Q9S2Te3oPc9k%2BREJTN3Kves4kLUI%2FCP%2BSvUgl%2BCvSXmrJEGvWlBZtVzRBp2CrFC0OQz5rRHDaVNgoyjhRXrBb1dawMN10pN0h7TMFQNgPP23upoKMoHOVmEVWjIJB24ZjjDWqez3JEbK%2FhdAJVE8BgdMvzbpIQkPG9C1UvrGzBDhrOookFecQfP6N1fg9MWXyVwEHM%2B8dEHK64XGO0qx4JPFYKCPOOUPZrrDCnLdHtdBYXeqImHzT7CEb4gRViFvwU1sYtCZdNpB9ommoSj4MvhDtWVPwSl4ViSc%2FQTM%2Ba12%2BCJyqD563E7CBuH7vHGgfYmC3Gp1tBdBEkP5qSzJlzSmGz%2Bks%2B3QCHlSf9WzpGowWC8qBNfCtyAQLR9acXi4lkLAeWqi3%2BkrTqs&sz=w512)  
     
    
  **Solução**Portanto, por gentileza, mapeie a customização que é pontada no errorlog, verifique os pontos acima esclarecidos e corrija esse cenário.  
   

  ***Saiba Mais:***

  + [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
  + [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
  + <https://tdn.totvs.com/display/public/framework/MenuDef>
  + <https://tdn.totvs.com/pages/releaseview.action?pageId=745762400>
