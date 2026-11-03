---
article_id: 360035248473
category: GPE - eSocial - Não Periódicos
content_hash: 644280791fcda48767f3d9068c76c5733dc6876db6b2c7b5db8ce81b431c48ef
fetched_at: '2026-06-28T22:45:04.626174+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2200/S-2299 - Funcionário xxxxxx não
  enviado ao TAF, Erro[000002]: Filial não cadastrada no Cadastro de complemento de
  empresa do TAF'
type: support-article
updated_at: '2026-06-16T13:34:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035248473-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2299-Funcion%C3%A1rio-xxxxxx-n%C3%A3o-enviado-ao-TAF-Erro-000002-Filial-n%C3%A3o-cadastrada-no-Cadastro-de-complemento-de-empresa-do-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262155400599) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
No módulo Gestão de Pessoal, ao tentar realizar transferência entre empresas com RAIZ de CNPJ diferente, é apresentada a mensagem: Funcionário xxxxxx não enviado ao TAF, Erro[000002]: Filial não cadastrada no Cadastro de complemento de empresa do TAF  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois não existe o cadastro de empresa no complemento cadastral do TAF.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acessar o módulo Totvs Automação Fiscal(**SIGATAF**).  
*Caminho SIGATAF: atualizações > Configs.Taf > Complemento Cadastral*  
  
2. Verificar se existe a empresa para qual está sendo enviado o funcionário, caso não exista será necessário incluir o cadastro da empresa e efetuar o envio do evento **S-1000** para o governo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045128314)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Perguntas frequentes FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
