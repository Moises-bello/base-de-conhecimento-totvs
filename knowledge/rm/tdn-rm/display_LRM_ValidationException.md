---
content_hash: e53af5b6dd9c99ed7be6280307977273f03c9ea2ed5b61bf15d0c5aa1f252796
fetched_at: '2026-06-29T00:08:49.523034+00:00'
page_id: '330839112'
product: rm
source: tdn-rm
title: ValidationException
type: documentation
url: https://tdn.totvs.com/display/LRM/ValidationException
version: 1
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Auxiliar na implementação/manutenção do Snowden.

# Execução:

---

        Existem diversas formas de subir uma exceção no RM. Muitas vezes é utilizado RMSException.Throw(...), throw new RMSApplicationException(...) ou até mesmo throw new Exception(...) para levantar uma exceção de validação da aplicação.

        No caso acima, a Hora Inicial deve ser maior que a Hora Final. Com o código acima, o resultado na tela será a imagem abaixo:

        Onde será exibido o botão para reportar o erro para TOTVS além de uma tela de erro para o usuário.

        Alterando o throw da Exception para RMSValidateException, estaremos informando a Lib que se tratada de uma exceção tratada.

        Assim, o botão de reportar para TOTVS não será exibido e a tela será apresentada como uma validação e não um erro do sistema.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** ValidationException

falsefalse

**Status:** Finalizado

false

**Data:** 15/01/2018

false

**Autores:**
