---
content_hash: d6bbc0908e4d206e49da5fe655567022e510ed4afe7daeff0f23ebb5f08d648a
fetched_at: '2026-06-29T00:10:32.665584+00:00'
page_id: '527391833'
product: rm
source: tdn-rm
title: RMFIS00002_REINF R-2030 / R-2040 – Recursos Recebidos/Repassados - Associação
  Desportiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527391833
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.27 |
| **Ocorrência:** | Eventos R-2030 / R-2040 – Recursos Recebidos/Repassados - Associação Desportiva |
| **Ambiente:** |  |
| **Passo a passo:** | **Evento R-2030**  **Conceito do evento**: Evento em que são prestadas informações relativas aos recursos recebidos a título de patrocínio, licenciamento de uso de marcas e símbolos, publicidade, propaganda e transmissão de espetáculos desportivos por associação desportiva que mantém equipe de futebol profissional. **Quem está obrigado**: Associação desportiva que mantém equipe de futebol profissional, quando receber recursos a título de patrocínio, licenciamento de uso de marcas e símbolos, publicidade, propaganda e transmissão de espetáculos desportivos. **Pré-requisitos**: Evento “R-1000 - Informações do Contribuinte”.    **Evento R-2040**  **Conceito do evento**: Evento em que são prestadas as informações relativas aos recursos repassados a título de patrocínio, licenciamento de uso de marcas e símbolos, publicidade, propaganda e transmissão de espetáculos desportivos, inclusive no caso do concurso de prognóstico de que trata a Lei nº 11.345/2006, para associação desportiva que mantém equipe de futebol profissional. **Quem está obrigado**: Empresa que repassou recursos para associação desportiva que mantém equipe de futebol profissional. **Pré-requisitos**: Evento “R-1000 - Informações do Contribuinte”. 121º Passo1º Passo Necessário habilitar o parâmetro "Movimento de Repasse EFD Reinf.  Acessar o TOTVS Gestão de Estoque, Compra e Faturamento. Acesse o menu Ambiente | Parâmetros | Gestão de Estoque, Compra e Faturamento | edite o tipo de movimento e acesse a etapa Etapa 61 - Fiscal - Dados Fiscais   Imagem  32º Passo2º Passo Necessário preencher corretamente a Classificação Tributária, no "Anexo | Dados Fiscais" (Cadastro da Filial) conforme imagem:   Imagem    43º Passo3º Passo O movimento deve possuir o tributo INSS informado.  Encerrar o período de apuração do tributo INSS e criar o evento totalizador R-5011   * SPED | EFD-Reinf | Eventos Periódicos   Selecione o evento, acesse o menu "Processos | EFD-Reinf - Gerar Eventos" conforme imagem:   Imagem  54º Passo4º Passo Selecione o evento criado, R-2010/2020, menu "Processos | Transmitir Evento".  Após transmitir o evento, selecione o evento transmitido e acesse o menu "Processos | Consultar Evento" para visualizar o retorno da receita.   Imagem  65º Passo5º Passo Ao editar o evento é possível visualizar a Identificação, Xml de Envio, Xml de Retorno e as Origens do Evento conforme imagem:   Imagem |
| **Observações:** |  |
