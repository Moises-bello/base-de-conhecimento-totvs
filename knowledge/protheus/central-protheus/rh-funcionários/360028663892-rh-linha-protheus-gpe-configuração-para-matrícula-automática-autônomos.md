---
article_id: 360028663892
category: RH - Funcionários
content_hash: e37f505a5941621fcc89f48073873e25835633e241fb62629983167912b699cd
fetched_at: '2026-06-28T22:43:27.708168+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração para Matrícula Automática  Autônomos
type: support-article
updated_at: '2025-09-29T19:22:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028663892-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-Autom%C3%A1tica-Aut%C3%B4nomos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Configuração para **Matrícula Automática de Autônomos**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.17  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1 - **MV\_MATRICU,** configure com **1 (Por Filial)** ou **2 (Por Empresa)**. Neste exemplo utilizaremos como **1, para que o sistema traga automático por Filial;**Mais informações sobre o **MV\_MATRICU:  
[Parâmetro MV\_MATRICU](http://tdn.totvs.com/download/attachments/201746766/GPE_BT_Atualizacao_do_parametro_MV_MATRICU_BRA_TQDOTV.pdf?version=1&modificationDate=1442954553000&api=v2)**[![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029797591/mceclip0.png)](http://tdn.totvs.com/download/attachments/201746766/GPE_BT_Atualizacao_do_parametro_MV_MATRICU_BRA_TQDOTV.pdf?version=1&modificationDate=1442954553000&api=v2)

2 - **MV\_MATAUT** – Indica a partir de **qual matricula deve iniciar o cadastramento dos autônomos.** Por padrão este parâmetro vem com **900000**, ou seja, o sistema vai iniciar as matrículas **a partir desse código.** Caso queira que siga a **mesma numeração dos funcionários (GPEA010)**, deixe o parâmetro em **branco;**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029797731/mceclip2.png)

3 - Nesse primeiro exemplo, utilizaremos o parâmetro **MV\_MATAUT** em **branco**, para seguir a **mesma numeração dos funcionários;**

**Observação: Somente funcionará seguindo a mesma sequência dos funcionários, caso não exista nenhuma matrícula com código 900000 ou superior. Se o sistema encontrar alguma matrícula a partir desse código na SRA, não será possível seguir a mesma sequência de matrículas de funcionários, sempre puxará a última a contar do código 900000.**4 - Deixe o campo **RA\_MAT** **sem validação** no Campo **Inic. Padrão** através do Configurador;  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029797791/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029807692/mceclip4.png)

5 - Para gerar a próxima matrícula, o sistema verifica a SRA e adiciona +1. Por exemplo, a **última matrícula da SRA** no exemplo abaixo, da filial **D MG 01 é 200775**. Ao incluir um novo autônomo, o sistema trará a próxima matrícula que é **200776;**  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029807732/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029807772/mceclip6.png)

6 - Neste segundo exemplo, utilizaremos o parâmetro **MV\_MATAUT *default* (900000)**, para seguir uma **numeração diferente dos funcionários;**  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029797911/mceclip7.png)

A **última matrícula da SRA de Autônomo** no exemplo abaixo, da filial **D MG 01 é 963023**. Ao incluir um novo autônomo, por conta da configuração do parâmetro MV\_MATAUT (tela acima) o sistema trará a próxima matrícula que é **963024**, seguindo a última numeração cadastrada para autônomos, diferenciando das matrículas dos funcionários.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029797931/mceclip8.png)  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029797971/mceclip9.png)  
  
  
**Importante: Caso perceba que na inclusão de um autônomo, não está seguindo a sequência conforme o exemplo acima, ou seja, está pulando numeração de matrícula, possivelmente possui algum funcionário cadastrado pela rotina GPEA010 com matrícula superior a 900000, logo, o Sistema vai considerar esta matrícula para então somar +1.   
  
Exemplo:** Ao entrar na rotina **GPEA265 - Contribuinte Individual**, a **última matrícula que pode ser vista no *grid* é 900005**, quando é feita uma inclusão, entende-se que a próxima matrícula de autônomo **seria 900006**, porém **traz 900010**, isso ocorre pois se avaliar a **SRA** no banco de dados, possivelmente já **existem as matrículas 900006, 900007, 900008 e 900009** para algum funcionário, **não necessariamente um autônomo**, com isso, o sistema verifica que a última numeração **acima de 900000 é 900009 e soma +1**, trazendo então **900010 na inclusão, corretamente.**

**Saber Mais:**

[RH - Linha Protheus - GPE - Configuração para Matrícula automática de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028979231-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-autom%C3%A1tica-de-funcion%C3%A1rios?source=search)

[RH - Linha Protheus - GPE - Parâmetros envolvidos no processo de Configuração para Matrícula automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406900205975-RH-Linha-Protheus-GPE-Par%C3%A2metros-envolvidos-no-processo-de-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-autom%C3%A1tica?source=search)

[RH - Linha Protheus - GPE - Sistema pula numeração de matrícula quando cancelada inclusão de funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052983333-RH-Linha-Protheus-GPE-Sistema-pula-numera%C3%A7%C3%A3o-de-matr%C3%ADcula-quando-cancelada-inclus%C3%A3o-de-funcion%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Inclusão de funcionário com matrícula incorreta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051186933-RH-Linha-Protheus-GPE-Inclus%C3%A3o-de-funcion%C3%A1rio-com-matr%C3%ADcula-incorreta-?source=search)
