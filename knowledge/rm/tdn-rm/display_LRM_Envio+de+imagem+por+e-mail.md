---
content_hash: bce2257fdf34d37c6f470e0774eeda571c67fcd5b31a1298916852dbb5931ab7
fetched_at: '2026-06-29T00:05:58.772513+00:00'
page_id: '187829055'
product: rm
source: tdn-rm
title: Envio de imagem por e-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+imagem+por+e-mail
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Fórmula Visual |
| **Subprocesso** | **:** | Utilizando a atividade "Envio de E-mail" |
| **Data da publicação** | **:** | 27/06/2014 |

**Objetivo:**A finalidade da atividade de "Envio de E-mail" como o próprio nome já diz é enviar e-mail através da fórmula visual.  
 Primeiramente é necessário arrastar a atividade "Envio de E-mail" para o "fluxo de trabalho" sequencial em sua fórmula visual.

|  |
| --- |
|  |

Após atividade ter sido adicionada ao fluxo de trabalho é necessário configurar as propriedades da atividade.

|  |
| --- |
|  |

Neste exemplo iremos enviar um e-mail com uma imagem anexa.

|  |
| --- |
| **Propriedades**  Assunto: Deve ser preenchido com o assunto do e-mail.  Texto do e-mail: Deve ser preenchido com o corpo do e-mail.  Destinatários: Lista de e-mails que deseja para quem deseja enviar.  Remetente: Quem irá enviar o e-mail.(Usuário/Coligada/ColigadaGlobal) |

##### Anexo

No exemplo abaixo foi utilizado a atividade **"Consulta SQL"**, onde a consulta sql associada a atividade retornará uma imagem do banco de dados.Para mais informações sobre esta atividade acesse [Consulta SQL](http://tdn.totvs.com/x/hJi2C).

Após adicionar e configurar a atividade **"Consulta SQL"** no fluxo de trabalho é necessário configurar as propriedades **"Anexar Arquivo"** e **"Nome do Arquivo"** da atividade **"Enviar E-mail"**.

|  |
| --- |
| A propriedade "Nome do Arquivo" deve conter a extensão que o arquivo receberá ao ser anexado ao e-mail. Conforme no exemplo o arquivo anexo terá a extensão **".JPG"** |

Como é a consulta sql que irá me retornar a imagem, é necessário associar a propriedade "Anexar Arquivo" os atributos da atividade "Consulta SQL" criada.

Para realizar a associação, de um duplo clique no ícone  da propriedade "Anexar Arquivo".

|  |
| --- |
|  |

Expanda a atividade "Consulta SQL"

|  |
| --- |
| Clique em OK para que o atributo seja inserido na propriedade da atividade.  **Obs:** A propriedade Item foi setada como Item["Imagem"] pois é este o campo que é retornado da minha consulta sql. |

|  |
| --- |
| Salve sua fórmula visual. |

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
