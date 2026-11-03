---
article_id: 360035247973
category: GPE - eSocial - Não Periódicos
content_hash: e66254a836fd9331e1416ae3c5d64d67a03970ed1bab916de023ca6bc22bb3a5
fetched_at: '2026-06-28T22:45:04.525836+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Funcionários devem estar vinculados
  a uma filial ou obra própria da empresa
type: support-article
updated_at: '2026-06-16T13:35:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035247973-RH-Linha-Protheus-GPE-eSocial-S-2200-Funcion%C3%A1rios-devem-estar-vinculados-a-uma-filial-ou-obra-pr%C3%B3pria-da-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262176622231) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
No módulo Gestão de Pessoal, ao tentar realizar o envio do evento S-2200 para o TAF, ocorre o erro:   
Funcionários devem estar vinculados a uma filial ou obra própria da empresa. Verifique Dados da Filial - Módulo **SIGACFG**. Os funcionários da(s) filial(is) abaixo estão vinculados a uma sub-empreitada ou os dados da obra não foram encontrados na tabela **F0F**, por isso não serão integrados.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esse incidente ocorre para casos que a empresa se trate de  Cadastro de Atividade Econômica da Pessoa Física (**CAEPF**), o erro ocorre pois não existe o cadastro da empresa na tabela **F0F** rotina **FISA137.**  
  
**Solução**  
1. Verificar no módulo configurador(**SIGACFG**) se existe a filial cadastrada e verificar na aba complementos se o campo **Produtor Rural** esta preenchido;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045985653)  
  
2. Verificar no módulo Livros Fiscais(**SIGAFIS**) no menu **>**Atualizações **>**Cadastros **> Complemento de estabelecimento** se existe o cadastro da empresa configurado, caso não exista será necessário realizar o cadastro preenchendo os campos conforme cadastro da empresa.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045985873)  
  
Conheça a documentação completa:

* [Produtor Rural - Pessoa Física](http://tdn.totvs.com/x/qLqCEw)
* [Construtoras e Cadastro de Obras](http://tdn.totvs.com/x/9YCtEw)

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
