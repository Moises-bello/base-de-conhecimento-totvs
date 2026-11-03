---
article_id: 5294666975511
category: GPE - eSocial - Não Periódicos
content_hash: 7a3d852731282fe5fe7b1aa87d7db1d1943e91dd53bd5cf5cd502ace2d7ca899
fetched_at: '2026-06-28T22:45:04.488785+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como excluir cadastros duplicados
  no TAF
type: support-article
updated_at: '2026-06-16T13:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5294666975511-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-excluir-cadastros-duplicados-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827964386199) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Identifiquei no TAF cadastros duplicados referente o mesmo trabalhador, qual devo excluir?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Quando for identificado **mais de um registro no TAF referente o mesmo funcionário**, mesma **competencia** e mesmo **evento**, deverá ser analisado se o colaborador possui múltiplos vínculos. Em caso negativo, não pode existir mais de um registro ativo para o mesmo CPF afim de evitar inconsistências na transmissão de futuros eventos.   
  
Para realizar a exclusão do evento S-2200, deverá primeiro ser verificado qual o código único no cadastro do funcionário (RA\_CODUNIC).   
[Como visualizar a matrícula do funcionário?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045583393)  
  
O código deve ser o mesmo existente no registro do TAF campo Matricula (C9V\_MATRIC) e no cadastro do governo.   
[Como visualizar a matrícula do funcionário no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059736733)  
[Como consultar os dados do funcionário no governo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042805974)   
  
Após identificado o cadastro incorreto, para realizar a exclusão posicione no registro e exclua direto no TAF.   
  
**Exemplo:**  
1. Identificamos a matrícula do funcionário no cadastro do SIGAGPE.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5294512088855)  
  
2. Ao filtrar os funcionário no TAF pelo CPF foram identificados dois registros com matrículas diferentes:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5294553895703)  
  
3. Neste cenário excluímos o segundo registro onde a matrícula estava diferente do SIGAGPE, porém deve ser avaliado também o registro no portal do governo: *![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5294610125335)***Saiba mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
