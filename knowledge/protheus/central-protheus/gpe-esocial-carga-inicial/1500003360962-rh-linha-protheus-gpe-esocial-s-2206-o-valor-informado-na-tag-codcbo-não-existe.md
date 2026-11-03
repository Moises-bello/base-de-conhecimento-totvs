---
article_id: 1500003360962
category: GPE - eSocial - Carga Inicial
content_hash: e070d7acd86c7e530ba56f704ddefe6a2bf0a52c46a6d7f3d0abc42abf202d16
fetched_at: '2026-06-28T22:45:03.342239+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - O valor informado na tag codCBO
  não existe na base de dados
type: support-article
updated_at: '2024-08-26T12:31:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003360962-RH-Linha-Protheus-GPE-eSocial-S-2206-O-valor-informado-na-tag-codCBO-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência**Ao confirmar uma alteração de contrato, apresenta a mensagem **O valor informado na tag codCBO não existe na base de dados.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**A mensagem de erro é apresenta, pois não existe o Código Brasileiro de Ocupação informado no TAF ou código inserido no campo não é um CBO válido de acordo com o Ministério do Trabalho e Emprego.**Solução**Para consultar se o CBO existe no TAF, acesse o módulo 84, no menu acesse Consultas > Tabelas Dinâmicas   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003469742)  
Busque pela tabela C8Z e em seguida, selecione o botão **Abrir *Browse***  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102290074)  
Faça a pesquisa do CBO com uma das opções existentes  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003469862)  
  
Se não existir o CBO desejado, verifique se seu ambiente está atualizado com o ultimo acumulado do esocial, disponível no *link* <https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>.  
  
Se estiver atualizado e ainda não apresentar o código CBO desejado, **verifique se foi executado atualização das tabelas autocontidas no TAF** [MP - SIGATAF - Como realizar a atualização das Tabelas Autocontidas no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGATAF-Como-realizar-a-atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-no-TAF-?source=search)  
  
**Saiba Mais:**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes) 

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
