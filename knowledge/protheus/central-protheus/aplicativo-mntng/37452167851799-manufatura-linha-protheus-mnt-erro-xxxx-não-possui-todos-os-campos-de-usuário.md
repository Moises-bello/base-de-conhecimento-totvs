---
article_id: 37452167851799
category: 'Aplicativo MNTNG '
content_hash: fb60f44ce35bce81d2357a167069e863831c5fb179e095d0ae2753fe6e1478df
fetched_at: '2026-06-28T22:42:37.793539+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - Erro: XX/XX Não possui todos os campos
  de usuário'
type: support-article
updated_at: '2026-01-28T12:31:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37452167851799-Manufatura-Linha-Protheus-MNT-Erro-XX-XX-N%C3%A3o-possui-todos-os-campos-de-usu%C3%A1rio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37452184879895)*** Tempo aproximado para leitura: **00:01:50 min**  
  
**Ocorrência**  
Ao tentar realizar o processo de **login** no **MNTNG** é apresentado o **Erro: XX/XX Não possui todos os campos de usuário.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Causa**  
Asituação acontece porque alguma tabela que está relacionada aos processos do **MNTNG** está sem os campos de *log* de usuário necessários para a utilização do aplicativo;   
  
**Solução**  
Revise todas as tabelas relacionadas ao **MNTNG** listadas em [MNT 0046 Tabelas envolvidas no MNT NG](https://tdn.totvs.com/display/PROT/MNT+0046+Tabelas+envolvidas+no+MNT+NG) e garanta que os campos reservados de **Log de Inclusão** e **Log de Alteração** estão presentes no dicionário de dados das tabelas e na estrutura real da tabela. Para informações de como realizar a configuração dos campos de Log, verifique [MNT 0003 Como configurar os campos de log de usuário?](https://tdn.totvs.com/pages/viewpage.action?pageId=446696488)  
  
Caso a mensagem continue sendo apresentada, siga os passos abaixo:

* Realize o processo de compilação do P.E [**DNG-14526 DT Ponto de Entrada para analisar informações do WS no app MNTNG**](https://tdn.totvs.com/pages/viewpage.action?pageId=642391631)
* Volte a realizar o processo de *login* no app **MNGNT** até a apresentação da mensagem **Erro: XX/XX Não possui todos os campos de usuário.**
* Acompanhe o histórico no arquivo **console.log** do serviço **Rest**. Deve apresentar mais informações da validação e quais tabelas estão com o problema, semelhante ao bloco a seguir.

```
2025-09-29T15:33:01.840000-03:00 4944|[15:33:01 - 4944 - mntnglog] Acesso a empresa/filial 010101
2025-09-29T15:33:10.216000-03:00 4944|[15:33:10 - 4944 - mntnglog] Emp.: 01 - tabelas sem campos de usuario: CTT  SA2  SB2
```
