---
article_id: 360028933251
category: GPE - eSocial - Periódicos
content_hash: 7db00c1e66a8cdd95cda0cda9bad476b568a601afa643a3d6deb16074ebdbb71
fetched_at: '2026-06-28T22:45:09.941684+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial/DCTFWEB - Salário-Maternidade referente
  a Folha Mensal pago pela empresa e sua Compensação na DCTFWEB (LEI nº 10.710/2003)
type: support-article
updated_at: '2025-07-21T14:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028933251-RH-Linha-Protheus-GPE-eSocial-DCTFWEB-Sal%C3%A1rio-Maternidade-referente-a-Folha-Mensal-pago-pela-empresa-e-sua-Compensa%C3%A7%C3%A3o-na-DCTFWEB-LEI-n%C2%BA-10-710-2003
---

**Ocorrência**eSocial/DCTFWEB - Salário-Maternidade referente a Folha Mensal pago pela empresa e sua Compensação na DCTFWEB (LEI nº 10.710/2003)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 11.80  
  
**Causa**Conforme o manual da DCTFWEB a compensação do salário-família e salário-maternidade deve ocorrer automaticamente, porém isso ocorre quando os eventos foram enviados de forma lógica,  cronológica e preenchido corretamente (Exemplo: S-2200, S-2230, S-1200, etc).  
Fonte: <http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/DCTFWeb/>  
**Solução****PASSO 1:**Para o eSocial foram criados novos IDs de Cálculo que proporcionalizam o valores relacionados ao período de Licença Maternidade, segue o Boletim Técnico para tal parametrização.  
  
**[Novos ID´s para atender exigências legais](http://tdn.totvs.com/pages/viewpage.action?pageId=358452691)**  
**PASSO 2:** Os IDs de cálculo já existentes e os mencionados no link acima deverão ser configurados com a Natureza e Código de Incidência devidos nessa situação e o RET (Governo) compensará automaticamente os valores da Contribuição devida pela empresa na **DCTFWEB**.  
  
**No Leiaute do eSocial 1.0 em sua página 14 é informado a tabela quem constam todos os códigos de natureza de rubrica previstos pelo eSocial:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10322373742615)  
 **No Anexo I do Leiautes do eSocial versão 1.0 a Tabela 3, pág. 14, traz todas as Naturezas mais comuns nessa situação:**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10322650782359)  
  
**No Leiaute do eSocial 1.0 em sua página 14 é informado os Códigos de Incidência de Contribuição Previdenciária que devem ser informados no evento S-1010, para os casos de licença maternidade os mais comuns são os sinalizados abaixo:**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10323445521943)  
  
Em caráter exemplificativo, abaixo demonstraremos um Trabalhador que iniciou a licença-maternidade em 15/01/2019.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029763331)  
  
No cálculo do GPE de 01/2019 o Sistema proporcionalizou o pagamento dos dias de salário do mês em duas Verbas, a de ID "0031 - Salário Mensalista" e ID "0040 - Salário Maternidade".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029773472)  
  
Segue abaixo um EXEMPLO das informações utilizadas no evento S-1010, lembrando que natureza da Verba e incidência tributária é algo particular e responsabilidade de cada Empresa.  
  
Verbas 112 - Salário Mensalista (ID 0031) - 13 dias = R$ 3.900,00  
**Natureza: 1000 - Salário, vencimento, soldo ou subsídio****In. Tr. Inss: 11 - Base de cálculo das contribuições sociais - Mensal**  
Verba de Salário Maternidade (ID 0040) - 17 dias = R$ 5.100,00   
**Natureza: 4050 - Salário maternidade - Mensal  
In. Tr. Inss: 21 - Base de cálculo das contribuições sociais - Salário maternidade - Mensal, pago pelo Empregador;**  
A licença-maternidade não muda nada na tributação do Trabalhador, só que o seu valor é abatido no total de Contribuição Previdenciária devido pela Empresa.  
  
Ou seja, o governo vai entender que essa verba se trata de Salário referente ao período de Licença-Maternidade e que ela entra na base de cálculo de INSS Mensal, porém, devido ao código de incidência de INSS ser 21, o governo também vai entender que esse valor deverá ser abatido da contribuições previdenciária do empregador com base na LEI nº 10.710/2003, mas isso não muda em nada o desconto do Trabalhador.  
  
Segue abaixo um print do evento S-5001 retornado após enviar o evento S-1200 de uma Trabalhador de licença-maternidade com as verbas configuradas conforme demonstrado acima. A Base de Cálculo vem correta e ele também destaca o valor referente ao Salário Maternidade e dessa forma isso será demonstrado e abatido na DCTFWEB.  
  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029767671)**  
  
**OBSERVAÇÃO:** Vale ressaltar que esse é um cenário **exemplificativo**, mesmo a documentação retratando o Salário Maternidade Mensal a lógica se aplica ao 13º Salário e que as incidências e naturezas deverão ser analisadas internamente por cada empresa, sempre observando os valores de médias, sobre horas, sobre valores, periculosidade e etc.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:

[MP - GPE - eSocial/DCTFWEB - Salário-Maternidade referente a 13º Salário pago pela empresa e sua Compensação na DCTFWEB (LEI nº 10.710/2003)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017423592)

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
