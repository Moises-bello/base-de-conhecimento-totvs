---
article_id: 360035241573
category: GPE - eSocial - Não Periódicos
content_hash: 8140ae7282d494465debe5aebe1d54c282450aada132355c3afdbdda015e9a32
fetched_at: '2026-06-28T22:45:04.565614+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Quando ocorre uma transferência
  há alteração da Matricula do eSocial
type: support-article
updated_at: '2026-06-16T10:40:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035241573-RH-Linha-Protheus-GPE-eSocial-S-2200-Quando-ocorre-uma-transfer%C3%AAncia-h%C3%A1-altera%C3%A7%C3%A3o-da-Matricula-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17654749223575) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Quando ocorre uma transferência há alteração da Matricula do eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Pode 'SIM' haver a mudança da Matricula do eSocial, porém depende do tipo de Transferência.  
A Matricula do eSocial é aquela registrada nos campos **RA\_CODUNIC** e **C9V\_MATRIC** do Protheus que são únicos abaixo de uma mesma raiz de CNPJ e vinculado a um CPF específico, porém quando um CPF tem mais de um registro/categoria é criado uma Matrícula para cada registro/categoria.  
  
**1. Se a transferência for entre Empresas da mesma raiz de CNPJ (Filial)**para o Sistema Protheus e para o eSocial são mantidas a mesma Matricula do eSocial;  
  
Nessa situação o Sistema cria uma cópia do evento S-2200 do Trabalhador no TAF (tabela C9V), porém com o campo Filial registrado na Filial Destino e também cria um evento S-2206 para esse Trabalhador informando a alteração de CNPJ do local de trabalho. Esse evento S-2206 é o que deve ser transmitido ao eSocial para informar a transferência.  
  
Para mais informações acesse o artigo: [RH - Linha Protheus - GPE - eSocial - S-2206 - Porque o sistema não altera a matricula do trabalhador no TAF quando ocorre uma transferência entre filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009469571).  
  
**2. Se a transferência for entre Empresas de raiz de CNPJ diferente (Grupo econômico)**, nessa situação o Trabalhador é demitido da Empresa origem com um motivo específico e é admitido na Empresa Destino com a Sucessão de Vínculos, porém, nessa situação pode haver a alteração da Matricula do eSocial.  
  
Quando ambas Empresas estão no mesmo ambiente do Protheus basta utilizar a rotina de Transferência do SIGAGPE que o Protheus criar um evento S-2299 na Empresa origem e um evento S-2200 na Empresa destino.  
  
Quando as empresas estão no Protheus, mas em Bases/Ambientes diferentes verifique o artigo: [RH - Linha Protheus - GPE - eSocial - S-2200/S-2299 - Como realizar Transferências no Protheus com SIGAMAT/Bases/Ambientes diferentes e Empresas de CNPJ raiz diferente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035240973)  
  
Quando a transferência é para uma Empresa que não utiliza o Protheus verifique o artigo: [RH - Linha Protheus - GPE - eSocial - S-2299 - Preciso fazer a Transferência de trabalhadores do Protheus para uma empresa que não utiliza o Protheus, como fazer isso no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023167651)  
  
**IMPORTANTE: Para entender a diferença entre Filial e Empresas de mesmo grupo econômico para o eSocial acesse o artigo abaixo:**[RH - Linha Protheus - GPE - eSocial - Qual a diferença entre Filial e Empresas do mesmo grupo econômico para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034775274)  
  
 **Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
